#!/usr/bin/env python3
#
#
# Copyright (c) 2021 B Tasker
#

import sys
from scapy.all import *


def pkt_callback(pkt):
    ''' Callback function to dump out the payload

    It might seem a bit redundant to pass the payload into `bytes` and
    immediately decode it. The reason is that it'll otherwise technically
    be raw, but print out as if it were bytes
    '''

   p = bytes(pkt[UDP].payload)
   print(p.decode())



sniff(iface='eth0', filter=f'udp port {sys.argv[1]}', prn=pkt_callback, store=0)
