#!/bin/bash

#
# Copyright (C) 2022 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

set -e

function start_syslog_ng ()
{
    local sng_dir="/var/lib/samba/syslog-ng"
    local sng_persist="${sng_dir}/syslog-ng.persist"

    # Keep the persist file next to the disk-buffer files: both live in the
    # persistent volume, so syslog-ng reuses its queue after a container
    # recreation instead of leaking a new .qf file every time.
    mkdir -vp "${sng_dir}"

    # Without the persist file no .qf can be referenced: any leftover queue is
    # an orphan from a previous container instance and can be discarded.
    if [[ ! -f "${sng_persist}" ]]; then
        rm -fv "${sng_dir}"/*.qf
    fi

    syslog-ng -F --no-caps --persist-file "${sng_persist}" &
}

function domain_controller_role ()
{
    ntp_signd="/var/lib/samba/ntp_signd"
    extra_args=()
    if [[ -n "${DNS_FORWARDER}" ]]; then
        extra_args+=("--option=dns forwarder=${DNS_FORWARDER}")
    fi

    if [[ ! -d "${ntp_signd}" ]]; then
        mkdir -v -m 0750 "${ntp_signd}"
    fi
    chgrp -c _chrony "${ntp_signd}"

    samba -F --debug-stdout "${extra_args[@]}" &
    chronyd -d -x &
    recycle run_daemon &
    wsdd -i "${IPADDRESS}" -d "${NBDOMAIN}" &
    start_syslog_ng
    wait -n
    exit $?
}

function member_server_role ()
{
    recycle run_daemon &
    wsdd -i "${IPADDRESS}" -d "${NBDOMAIN}" &
    smbd -F --debug-stdout &
    winbindd -F --debug-stdout &
    nmbd -F --debug-stdout &
    start_syslog_ng
    wait -n
    exit $?
}

#
# Expand configuration and start services
#

expand-config

if [ $# -gt 0 ]; then
    exec "${@}"
fi

testparm -s 2>/dev/null
if [ "${SERVER_ROLE}" == "member" ] ; then
    member_server_role
else
    domain_controller_role
fi
