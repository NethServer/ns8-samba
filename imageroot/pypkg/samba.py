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
