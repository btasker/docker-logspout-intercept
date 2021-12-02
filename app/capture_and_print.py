#!/usr/bin/env python3
#
#
# Copyright (c) 2021 B Tasker
#

import docker
import sys
from scapy.all import *


def prnt_line(pkt):
    ''' Callback function to dump out the payload

    It might seem a bit redundant to pass the payload into `bytes` and
    immediately decode it. The reason is that it'll otherwise technically
    be raw, but print out as if it were bytes
    '''
    p = bytes(pkt[UDP].payload)
    print(p.decode(), end='')


def get_syslog_port_from_container(cont):

    dockerClient = docker.from_env()
    client = docker.APIClient(base_url='unix://var/run/docker.sock')

    logconf = client.inspect_container(cont)['HostConfig']['LogConfig']
    if logconf['Type'] != "syslog":
        return False

    # Return the port
    return logconf['Config']['syslog-address'].split(":")[-1]


port=sys.argv[1]
if not port.isnumeric():
    # We've been given a docker container name instead
    port = get_syslog_port_from_container(sys.argv[1])
    if not port:
        print("Error - container {sys.argv[1]} is not using Syslog")
        sys.exit(1)



sniff(iface='eth0', filter=f'udp port {port}', prn=prnt_line, store=0)
