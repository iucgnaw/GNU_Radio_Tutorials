#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xmlrpc.client import ServerProxy
import time
xmlrpc_control_client = ServerProxy('http://'+'localhost'+':8000')
freq_steps = [6e3, 11e3, 2e3, 14e3, 4e3, 3.5e3]
while True:
    for freq in freq_steps:
        print("retuning to:",freq/1000,"kHz")
        xmlrpc_control_client.set_rmt_freq(freq)
        time.sleep(2)
