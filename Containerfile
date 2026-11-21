# Stage 1: Base Ubuntu + Samba image
FROM docker.io/library/ubuntu:resolute AS ubuntu-samba-base

ENV DEBIAN_FRONTEND=noninteractive

# Packages are not pinned: Ubuntu removes old builds from the archive.
# The fake pin below only makes Renovate open a PR on new Samba builds.
# renovate-ubuntu: suite=noble-updates
# samba=2:4.19.5+dfsg-4ubuntu9.8
RUN set -e \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        samba \
        samba-ad-dc \
        samba-ad-provision \
        winbind \
        krb5-user \
        iputils-ping \
        bzip2 \
        ldb-tools \
        chrony \
        bind9-dnsutils \
        acl \
        attr \
        smbclient \
        libnss-winbind \
        rsync \
        plocate \
        wsdd \
        syslog-ng-core \
        syslog-ng-mod-sql \
        libdbd-pgsql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*.deb \
    && rm -rf /tmp/* /var/tmp/* \
    && find /usr/share/doc -depth -type f ! -name copyright -delete \
    && find /usr/share/man -type f -delete

# Stage 2: Samba DC image
FROM ubuntu-samba-base

# Copy entrypoint and other required files
COPY samba-dc/ /

# Move default smb.conf to backup
RUN mv -v /etc/samba/smb.conf /etc/samba/smb.conf.distro

# Set environment variables
ENV SAMBA_LOGLEVEL="1 auth_audit:0 auth_json_audit:0" \
    SAMBA_SHARES_DIR=/srv/shares \
    SAMBA_HOMES_DIR=/srv/homes \
    SERVER_ROLE=dc \
    DNS1ADDRESS=127.0.0.1

# Create required directories and perform system setup
RUN set -e \
    && mkdir -m 0755 -p "${SAMBA_SHARES_DIR}" "${SAMBA_HOMES_DIR}" \
    && chown -c root:root "${SAMBA_SHARES_DIR}" "${SAMBA_HOMES_DIR}" \
    && [ "$(id -u nobody)" = "65534" ] || (echo "Unexpected nobody uid value" && exit 1) \
    && [ "$(id -g nobody)" = "65534" ] || (echo "Unexpected nobody gid value" && exit 1) \
    && [ "$(getent group users | cut -d: -f3)" = "100" ] || (echo "Unexpected users gid value" && exit 1) \
    && echo "OS $(grep -E '^(NAME|VERSION)=' /etc/os-release)" \
    && echo "Samba $(samba -V)" \
    && mkdir -vp /var/lib/samba/skel.d \
    && sed -r -i '/^HOME_MODE/ s/\b0750\b/0700/' /etc/login.defs

# Define volumes
VOLUME ["/srv/shares", "/srv/homes", "/var/lib/samba", "/etc/samba"]

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
CMD []
