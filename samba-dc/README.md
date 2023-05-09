# samba-dc

This image provides a Samba domain controller with a basic file server
configuration. Read carefully the Samba Wiki section about [using a DC as
a file
server](https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller#Using_the_Domain_Controller_as_a_File_Server_.28Optional.29)
to understand its limitations.

## TCP/UDP ports

The container uses the following ports:

- `53/tcp`, `53/udp`, DNS
- `88/tcp`, `88/udp`, Kerberos
- `123/udp`, NTP
- `135/tcp`, End Point Mapper (DCE/RPC Locator Service)
- `137/udp`, NetBIOS Name Service
- `138/udp`, NetBIOS Datagram
- `139/tcp`, NetBIOS Session
- `389/tcp`, `389/udp`, LDAP
- `445/tcp`, SMB over TCP
- `464/tcp`, `464/udp`, Kerberos kpasswd
- `636/tcp`, LDAPS
- `3268/tcp`, Global Catalog
- `3269/tcp`,  Global Catalog SSL
- `49152-65535/tcp` Dynamic RPC Ports

## Volumes

- `config`, mounted on `/etc/samba`.
- `data`, contains Samba databases and the default `sysvol` and
  `netlogon` shares. Mounted on `/var/lib/samba`.
- `shares`, storage of shared folders, mounted on `/srv/shares`.
- `homes`, home directories, mounted on `/srv/homes`.

## Environment variables

The following environment variables are expected to run the normal
container services. Some commands can expect more variables: see the
individual command documentation for more information.

- `IPADDRESS`, bind services to this IPv4 address (in addition to 127.0.0.1)
- `PREFIXLEN`, if the network devices does not provide network information
  (e.g. VPN, point-to-point) set this variable to the netmask length. If
  this variable is set, NetBIOS is implicitly disabled.
- `NBDOMAIN`, the NT-style domain name
- `REALM`, the domain name for Kerberos and DNS configuration
- `DNS_FORWARDER`, if present its value is added as `dns forwarder` among
  samba startup options.
- `SAMBA_SHARES_DIR`, default `/srv/shares`: path to the volume containing
  shared folders. Do not change it! In any case do not put it under
  `/var/lib/samba` to avoid conflicts with the backup procedure.
- `SAMBA_HOMES_DIR`, default `/srv/homes`: path to the volume containing
  user home directories. Do not change it! In any case do not put it under
  `/var/lib/samba` to avoid conflicts with the backup procedure.
- `SAMBA_LOGLEVEL`, default `1`: value for the `log level` configuration
  directive.

## Custom configuration

To override the container configuration, write custom `smb.conf`
directives in the `include.conf` file, under the `config` volume root. It
corresponds to this container path:

    /etc/samba/include.conf

## `entrypoint.sh`

The container entrypoint in any case runs the `expand-config` command, to
properly initialize the container configuration files.

If any argument is passed to the container entrypoint it is interpreted as
a command to execute. This behavior is required to run `new-domain` and
`join-domain`.

If no arguments are passed, `init-shares` and `init-homes` are executed,
then the normal services are started:

- `samba`
- `chronyd`

## Commands

Commands are installed under `/usr/local/sbin`.

### `expand-config`

The `expand-config` command runs at the container entrypoint. It writes
the following configuration files, based on the values of the container
environment variables.

- `/etc/hosts`
- `/etc/krb5.conf`
- `/etc/samba/smb.conf`
- `/etc/resolv.conf`

### `init-shares` and `init-homes`

The `init-shares` and `init-homes` commands create the root directory for
shared folders and home directories, respectively. They ensure proper
ownership, permissions and Windows ACLs are set.

### `new-domain`

This command is designed to run as the container entrypoint argument. Eg.

    podman run --env=ADMINCREDS ... --volume data:/var/lib/samba:z ... samba-dc:latest new-domain

The Samba DC services are not started at all, instead the command clears
the `smb.conf` file and starts a new domain provision procedure. If the
procedure is successful the command terminates with `0` exit code and the
volumes are left ready for starting the DC.

Apart from common environment variables, it expects to read the
credentials of a `Domain Admins` member from the environment variable
`ADMINCREDS`. If that user does not exist, it is created, assigned the
password, and added to `Domain Admins` on the fly.

The `ADMINCREDS` environment variable format must be a base64-encoded TSV
record with this format:

    <ADMIN_NAME> <TAB> <ADMIN_PASSWORD>

Also the credentials of a service user are expected in the environment
variables `SVCUSER` and `SVCPASS`. This user is granted standard
privileges and its password is set with "no-expire" flag.

### `join-domain`

This command is designed to run as the container entrypoint argument. Eg.

    podman run --env=JOINADDRESS ... --volume data:/var/lib/samba:z ... samba-dc:latest join-domain

Similarly to `new-domain`, it expects the `ADMINCREDS` variable is
present. This time the credentials are presented to join a new DC to an
existing AD domain. The user must be already granted the domain join
permissions: usually a member of the `Domain Admins` group is used for
this purpose.

The additional `JOINADDRESS` variable must be contain the IP address of an
existing DC. It is used as container DNS resolver to run the join
procedure.

Like the `new-domain` command, if `join-domain` terminates with exit-code
`0` the volumes are left ready for starting the DC.

### `samba-add-share`

Create a new directory under `SAMBA_SHARES_DIR` and add it to the Samba
registry as a new share.

Adding a new share implicitly invokes `samba-reset-acls` on it. For the
command help type:

    samba-add-share -h

### `samba-remove-share`

Remove the share configuration from the Samba registry and erase the share
directory with all of its contents. The command takes just one argument:
the share name.

    samba-remove-share myshare1

### `samba-reset-acls`

Reset the ACLs of a shared directory and its contents. If the share was
created by `rsyncd-import-shares`, reset also the Samba share
configuration to NS8 defaults. For the command help type:

    samba-reset-acls -h

During the reset recursive procedure, the share is not accessible.

### `rsyncd-import-shares`

Starts a special Rsync server used by the NS7 migration tool.  It can
resolve user and group names and it supports Posix ACLs. Configuration
parameters are passed with RSYNCD_* environment variables, as defined in
the
[core/rsync](https://github.com/NethServer/ns8-core/blob/main/core/rsync/README.md)
container. Terminate the server by connecting to the `terminate` Rsync
module. When Rsync completes successfully, the command expects to read
shares metadata from standard input in TSV format to load them into the
Samba configuration registry.

### `validate-demote`

This command checks if the local DC is assigned some FSMO role. Run this
check before decommissioning the DC. Exit-code `2` means some FSMO role is
assigned to the DC.