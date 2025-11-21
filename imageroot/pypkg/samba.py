#
# Copyright (C) 2022 Nethesis S.r.l.
# http://www.nethesis.it - nethserver@nethesis.it
#
# This script is part of NethServer.
#
# NethServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# NethServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NethServer.  If not, see COPYING.
#

import ipaddress as ipm
import subprocess
import socket
import json
import dns.resolver
import sys
import agent
import os
import cluster.userdomains

class SambaException(Exception):
    pass

class IpNotPrivate(SambaException):
    pass

class IpNotAvailable(SambaException):
    pass

class IpBindError(SambaException):
    def __init__(self, ipaddr, message):
        self.ipaddr = ipaddr
        self.message = message
        super().__init__(self.message)

def ipaddress_check(ipaddress):
    """Run all checks together"""
    ipaddress_check_isprivate(ipaddress)
    ipaddress_check_isavailable(ipaddress)
    ipaddress_check_hasfreeports(ipaddress)
    return True

def ipaddress_check_isprivate(ipaddress):
    """The IP address must be in a private network class"""
    addr = ipm.ip_address(ipaddress)
    # See Python docs: https://docs.python.org/3.9/library/ipaddress.html#ip-addresses
    if not addr.is_private or addr.is_unspecified or addr.is_reserved or addr.is_loopback or addr.is_link_local:
        raise IpNotPrivate()

    return True

def ipaddress_check_isavailable(ipaddress):
    """The IP address is available and it is possible to bind a random port on it"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
                sk.bind((ipaddress, 0))
    except Exception as ex:
        raise IpNotAvailable(f"Address {ipaddress} bind failed: {ex}") from ex

    return True

def ipaddress_check_hasfreeports(ipaddress):
    """TCP ports for DC services are free on the given IP address"""
    for tcp_port in [53, 88, 636, 464, 445, 3268, 3269, 389, 135, 139]:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
                sk.bind((ipaddress, tcp_port))
        except Exception as ex:
            raise IpBindError(ipaddress, f"Address {ipaddress}:{tcp_port} bind failed: {ex}") from ex

    return True

def ipaddress_list(skip_wg0=False, only_wg0=False):
    proc = subprocess.run(["ip", "-j", "-4", "address", "show"], text=True, capture_output=True)
    try:
        joutput = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return []

    ipaddresses = []
    for iface in joutput:
        try:
            # skip wg0, as required by arguments
            if iface["ifname"] == "wg0" and skip_wg0:
                continue
            # skip non-wg0 interfaces, as required by arguments
            if iface["ifname"] != "wg0" and only_wg0:
                continue
            # skip interface without bcast address; wg0 is handled specially
            if iface["ifname"] != "wg0" and not 'BROADCAST' in iface["flags"]:
                continue
            # skip CNI interfaces
            if iface["ifname"].startswith('cni-'):
                continue
        except KeyError:
            pass

        ifip_list = [] # this list collects private ip addresses for iface
        for ainfo in iface['addr_info']:
            addr = ipm.ip_address(ainfo['local'])
            if addr.is_private and not (addr.is_unspecified or addr.is_reserved or addr.is_loopback or addr.is_link_local):
                altnames = ""
                if 'altnames' in iface:
                    altnames = f" ({', '.join(iface['altnames'])})"
                ifip_list.append({
                    "ipaddress": ainfo['local'],
                    "label": iface['ifname'] + altnames
                })
            else:
                # If the interface has at least a non-private
                # address, ignore it completely
                break
        else:
            # If the loop completes without breaking, add collected
            # ip addresses to the response list
            ipaddresses += ifip_list
    return ipaddresses

def validate_hostname(hostname, realm, nameservers=[]):
    rsv = dns.resolver.Resolver(configure=False)
    rsv.nameservers.extend(nameservers)
    try:
        resolve_ret = rsv.resolve(realm)
        print("DNS nameserver", resolve_ret.nameserver, file=sys.stderr)
        print("DNS authority", resolve_ret.response.authority, file=sys.stderr)
        print("Domain", resolve_ret.rrset.to_text(), file=sys.stderr)
    except dns.resolver.NoAnswer as ex:
        print("DNS error:", ex, file=sys.stderr)
        json.dump([{"field": "realm", "parameter": "realm", "value": realm, "error": "realm_dc_avail_check_failed"}], fp=sys.stdout)
        agent.set_status('validation-failed')
        sys.exit(6)
    except dns.exception.Timeout as ex:
        print("DNS error:", ex, file=sys.stderr)
        json.dump([{"field": "realm", "parameter": "realm", "value": realm, "error": "realm_dc_reachable_check_failed"}], fp=sys.stdout)
        agent.set_status('validation-failed')
        sys.exit(7)

    #
    # Check if the hostname is already registered in the DNS
    #
    try:
        hostname_resolve_ret = rsv.resolve(hostname + '.' + realm)
        print(agent.SD_ERR + f"DC hostname {hostname} is already in DNS!", hostname_resolve_ret.rrset.to_text(), file=sys.stderr)
        json.dump([{"field": "hostname", "parameter": "hostname", "value": hostname, "error": "hostname_check_failed"}], fp=sys.stdout)
        agent.set_status('validation-failed')
        sys.exit(11)
    except dns.resolver.NXDOMAIN:
        pass

def validate_ipaddress(ipaddress):
    try:
        ipaddress_check(ipaddress)
    except IpNotPrivate:
        agent.set_status('validation-failed')
        json.dump([{"field":"ipaddress","parameter":"ipaddress","value": ipaddress,"error":"ipaddress_private_check_failed"}], fp=sys.stdout)
        sys.exit(2)
    except IpNotAvailable:
        agent.set_status('validation-failed')
        json.dump([{"field":"ipaddress","parameter":"ipaddress","value": ipaddress,"error":"ipaddress_avail_check_failed"}], fp=sys.stdout)
        sys.exit(3)
    except IpBindError as ex:
        print(ex, file=sys.stderr)
        agent.set_status('validation-failed')
        json.dump([{"field":"ipaddress","parameter":"ipaddress","value": ex.ipaddr,"error":"ipaddress_bind_check_failed"}], fp=sys.stdout)
        sys.exit(4)

def push_vpn_routes():
    node_id = int(os.environ['NODE_ID'])
    rdb = agent.redis_connect()
    oip_address = ipm.ip_address(os.environ['IPADDRESS'])
    ocluster_network = ipm.ip_network(rdb.get('cluster/network'), strict=False)
    if not oip_address in ocluster_network:
        agent.tasks.run(
            agent_id='cluster',
            action='update-routes',
            data={
                'add': [{
                    "ip_address": os.environ['IPADDRESS'],
                    "node_id": node_id,
                }],
            },
            extra={"isNotificationHidden": True},
        )

def get_joinaddress():
    kdomain = os.getenv('DOMAIN', os.environ['REALM'].lower())

    rdb = agent.redis_connect()
    domains = cluster.userdomains.get_internal_domains(rdb)

    if not kdomain in domains:
        raise SambaException(f'Realm "{kdomain}" not found')

    for provider in domains[kdomain]['providers']:
        if provider['id'] != os.environ["MODULE_ID"]:
            break # DC found. Stop searching.
    else:
        # DC not found: error!
        raise SambaException(f'DC for "{kdomain}" not found')

    return provider['host']

def configure_samba_audit(sharename, enable_audit=True, log_failed_events=False):
    podman_exec = ["podman", "exec", "samba-dc"]
    setparm_cmd = podman_exec + ["net", "conf", "setparm", sharename]
    delparm_cmd = podman_exec + ["net", "conf", "delparm", sharename]
    enabled_success_operations = os.getenv("SAMBA_AUDIT_SUCCESS", "create_file unlinkat renameat mkdirat fsetxattr")
    enabled_failure_operations = os.getenv("SAMBA_AUDIT_FAILURE", "create_file unlinkat renameat mkdirat fsetxattr")
    set_audit_cmd = delparm_cmd + ["full_audit:success"]
    set_logfailed_cmd = delparm_cmd + ["full_audit:failure"]
    if enable_audit:
        set_audit_cmd = setparm_cmd + ["full_audit:success", enabled_success_operations]
        if log_failed_events:
            set_logfailed_cmd = setparm_cmd + ["full_audit:failure", enabled_failure_operations]
    agent.run_helper(*set_audit_cmd, stderr=subprocess.DEVNULL)
    agent.run_helper(*set_logfailed_cmd, stderr=subprocess.DEVNULL)

def configure_recycle(sharename, enable_recycle=True, recycle_retention=0, recycle_versions=False):
    if enable_recycle:
        agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "setparm", sharename, "recycle:repository", os.getenv("RECYCLE_REPOSITORY", ".recycle") + "/%U")
        if recycle_versions:
            agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "delparm", sharename, "recycle:versions")
        else:
            agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "setparm", sharename, "recycle:versions", "no")
        agent.run_helper("podman", "exec", "samba-dc", "recycle", "set_retention", sharename, str(recycle_retention))
        agent.run_helper("podman", "exec", "samba-dc", "recycle", "init_repository", sharename)
    else:
        agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "delparm", sharename, "recycle:repository")
        agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "delparm", sharename, "recycle:versions")
        agent.run_helper("podman", "exec", "samba-dc", "recycle", "del_retention", sharename)

def configure_browseable(sharename, browseable=True):
    if browseable:
        agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "delparm", sharename, "browseable")
    else:
        agent.run_helper("podman", "exec", "samba-dc", "net", "conf", "setparm", sharename, "browseable", "no")

def get_user_account_control(user):
    sambatool_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool']
    getdn_cmd = sambatool_cmd + ['user', 'show', user, '--attributes=userAccountControl']
    proc = subprocess.run(getdn_cmd, check=True, capture_output=True, text=True)
    output = proc.stdout.strip()
    # Extract the DN and userAccountControl value
    dn_str = None
    user_account_control = None
    for line in output.splitlines():
        if line.startswith("dn:"):
            dn_str = line
        elif line.startswith("userAccountControl:"):
            user_account_control = int(line.split(":", 1)[1].strip())
    if not dn_str or user_account_control is None:
        raise Exception("DN or userAccountControl not found")
    return dn_str, user_account_control

def set_user_account_control(dn_str, user_account_control, no_password_expiration):
    UF_DONT_EXPIRE_PASSWORD = 0x10000
    if no_password_expiration == True and not ( user_account_control & UF_DONT_EXPIRE_PASSWORD ):
        user_account_control |= UF_DONT_EXPIRE_PASSWORD # set the flag
    elif no_password_expiration == False and ( user_account_control & ~UF_DONT_EXPIRE_PASSWORD ):
        user_account_control &= ~UF_DONT_EXPIRE_PASSWORD # clear the flag
    else:
        user_account_control = None  # No change needed
    if user_account_control is not None:
        ldbmodify_cmd = ['podman', 'exec', '-i', 'samba-dc', 'ldbmodify', '-H', '/var/lib/samba/private/sam.ldb']
        ldbmodify_input = f'{dn_str}\nchangetype: modify\nreplace: userAccountControl\nuserAccountControl: {user_account_control}\n'
        subprocess.run(ldbmodify_cmd, input=ldbmodify_input, stdout=sys.stderr, check=True, text=True)

def get_ad_ldap_suffix() -> str:
    parts = os.environ["DOMAIN"].split(".")
    return "DC=" + ",DC=".join(parts)

def import_users(records: list, skip_existing: bool):
    LDAPSUFFIX = get_ad_ldap_suffix()
    ACTYPE = 0; ACID = 1; ACMEMBERS = 2; ACUAC = 3
    merge_existing = not skip_existing
    adb = _get_accounts()

    all_users = set() # imported user names (AD may have more..)
    mod_groups = dict() # new group membership mapping
    new_groups = set() # names of new groups

    # Accumulate LDIF changes
    ldif_changes = dict() # DB of LDIF changes, key is DN
    def ldif_prepare(user, att, val, op='replace'):
        dn = adb[user.lower()][ACID]
        ldif_changes.setdefault(dn, [])
        ldif_changes[dn].append((att, val, op))

    for rec in records:
        user = rec['user']
        all_users.add(user)
        pwd = rec.get('password', '')
        display_name = rec.get('display_name', user.title())
        must_change = rec.get('must_change_password') is True
        mail_address = rec.get('mail')

        # Accumulate changes for userAccountControl attribute (UAC)
        uac_set_flags = 0
        uac_clear_flags = 0
        if rec.get('locked') is True:
            uac_set_flags |= 0x2 # ACCOUNTDISABLED
        elif rec.get('locked') is False:
            uac_clear_flags |= 0x2 # ACCOUNTDISABLED
        if rec.get('no_password_expiration') is True:
            uac_set_flags |= 0x10000 # DONT_EXPIRE_PASSWD
        elif rec.get('no_password_expiration') is False:
            uac_clear_flags |= 0x10000 # DONT_EXPIRE_PASSWD

        # 1. Handle user creation and password reset with samba-tool
        if user.lower() in adb:
            if pwd and merge_existing:
                _reset_password(user, pwd)
            elif skip_existing:
                continue # next record
        else:
            _create_user(user, pwd)
            udn = f'CN={user},CN=Users,' + LDAPSUFFIX # Assuming default DN
            adb[user.lower()] = ('U', udn, [], 512)
            adb[udn.lower()] = ('U', user, [], 512)
        # 2. Prepare group sync information
        for gna in rec.get('groups', []) or []:
            if gna.lower() in adb:
                if gna.lower() in new_groups:
                    # gna must be created, annotate member:
                    gdn = adb[gna.lower()][ACID]
                    adb[gna.lower()][ACMEMBERS].append(user)
                    adb[gdn.lower()][ACMEMBERS].append(user)
                else:
                    # gna must be modified:
                    mod_groups.setdefault(gna, [])
                    mod_groups[gna].append(user)
            else:
                # gna must be created, initialize it:
                if _create_group(gna):
                    new_groups.add(gna.lower())
                    gdn = f'CN={gna},CN=Users,' + LDAPSUFFIX # Assuming default DN
                    adb[gna.lower()] = ('G', gdn, [user], 0)
                    adb[gdn.lower()] = ('G', gna, [user], 0)

        # Prepare LDIF changes
        ldif_prepare(user, 'displayName', display_name)
        ldif_prepare(user, 'mail', mail_address)
        if must_change:
            ldif_prepare(user, 'pwdLastSet', 0)
        uac = adb[user.lower()][ACUAC]
        ldif_prepare(user, 'userAccountControl', (uac | uac_set_flags) & ~uac_clear_flags)

    # 3. Add members to new groups:
    for newg in new_groups:
        _group_addmembers(newg, adb[newg][ACMEMBERS])
    # 4. Change members of existing groups:
    all_users_dn = { adb[u.lower()][ACID].lower() for u in all_users }
    for gna in mod_groups:
        new_members_dn = { adb[u.lower()][ACID].lower() for u in mod_groups[gna] }
        old_members_dn = { adb[u.lower()][ACID].lower() for u in adb[gna.lower()][ACMEMBERS] } & all_users_dn
        addparams = [ '--member-dn=' + gdn for gdn in new_members_dn - old_members_dn ]
        if addparams:
            _group_addmembers(gna, addparams)
        remparams = [ '--member-dn=' + gdn for gdn in old_members_dn - new_members_dn ]
        if remparams:
            _group_removemembers(gna, remparams)

    # 5. Apply LDIF changes:
    ldbmodify_cmd = ['podman', 'exec', '-i', 'samba-dc', 'ldbmodify', '-v', '-H', '/var/lib/samba/private/sam.ldb']
    proc = subprocess.Popen(ldbmodify_cmd, stdin=subprocess.PIPE, stdout=sys.stderr, text=True)
    for dn in ldif_changes.keys():
        if proc.stdin.closed:
            # Resume after error:
            proc = subprocess.Popen(ldbmodify_cmd, stdin=subprocess.PIPE, stdout=sys.stderr, text=True)
        changes = ldif_changes[dn]
        proc.stdin.write('dn: ' + dn + '\n')
        proc.stdin.write('changetype: modify' + '\n')
        for cht in changes:
            proc.stdin.write('-' + '\n')
            if cht[2] == 'replace':
                proc.stdin.write('replace: ' + cht[0] + '\n')
                proc.stdin.write(cht[0] + ': ' + str(cht[1]) + '\n')
        proc.stdin.write('\n')

def _group_addmembers(group, members):
    addmembers_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool', 'group', 'addmembers', group, *members]
    print(*addmembers_cmd, file=sys.stderr)
    proc = subprocess.run(addmembers_cmd, stdout=sys.stderr, text=True)
    return proc.returncode == 0

def _group_removemembers(group, members):
    removemembers_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool', 'group', 'removemembers', group, *members]
    print(*removemembers_cmd, file=sys.stderr)
    proc = subprocess.run(removemembers_cmd, stdout=sys.stderr, text=True)
    return proc.returncode == 0

def _create_group(group):
    addgroup_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool', 'group', 'create', group]
    proc = subprocess.run(addgroup_cmd, stdout=sys.stderr, text=True)
    return proc.returncode == 0

def _reset_password(user, password) -> bool:
    adduser_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool', 'user', 'setpassword', user]
    inputdata = password + "\n" + password + "\n"
    proc = subprocess.run(adduser_cmd, input=inputdata, stdout=sys.stderr, text=True)
    return proc.returncode == 0

def _create_user(user, password) -> bool:
    adduser_cmd = ['podman', 'exec', '-i', 'samba-dc', 'samba-tool', 'user', 'create', user]
    if not password:
        adduser_cmd += ['--random-password']
        inputdata = None
    else:
        inputdata = password + "\n" + password + "\n"
    proc = subprocess.run(adduser_cmd, input=inputdata, stdout=sys.stderr, text=True)
    return proc.returncode == 0

def _get_accounts() -> dict:
    """Returns account information indexed by DN and sAMAccountName. Each value is a tuple with:
    - Account type ("U" or "G"),
    - Account DN or name. If one is used as key, the other is set as second element of the triplet.
    - Array of member DNs, if type is G.
    - userAccountControl flags
    """
    v = lambda l: l.split(": ", 1)[1]
    accounts = dict()
    with subprocess.Popen([
            'podman', 'exec', '-i', 'samba-dc', 'ldbsearch',
            '-H', '/var/lib/samba/private/sam.ldb',
            '-b', get_ad_ldap_suffix(),
            '--paged',
            '(sAMAccountName=*)',
            'sAMAccountName',
            'member',
            'userAccountControl',
        ], text=True, stdout=subprocess.PIPE) as proc_ldbsearch:
            curna = None # current record name
            curdn = None # current record DN
            curmb = []   # current record members
            curty = 'U'  # current record type (User or Group)
            curac = 0    # current record UAC attribute
            for ldifline in proc_ldbsearch.stdout:
                ldifline = ldifline.rstrip("\n")
                if not ldifline:
                    # End-Of-Record
                    if curdn and curna:
                        accounts[curdn.lower()] = (curty, curna, curmb, curac)
                        accounts[curna.lower()] = (curty, curdn, curmb, curac)
                    curdn = None
                    curna = None
                    curmb = []
                    curty = 'U'
                elif ldifline.startswith("dn:"):
                    curdn = v(ldifline)
                elif ldifline.startswith("sAMAccountName:"):
                    curna = v(ldifline)
                elif ldifline.startswith("member:"):
                    curmb.append(v(ldifline))
                elif ldifline.startswith("userAccountControl:"):
                    try:
                        curac = int(v(ldifline))
                    except ValueError:
                        cuarc = 2 # ACCOUNTDISABLE
                elif ldifline == 'objectClass: group':
                    curty = 'G'
    return accounts