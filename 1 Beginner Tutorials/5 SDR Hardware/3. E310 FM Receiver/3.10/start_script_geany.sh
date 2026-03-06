#!/bin/sh

cleanup() {
    echo '[INFO] Stop requested'
    pkill -f RX_FM_USRP_UDP.py
    exit 0
}

trap cleanup INT TERM

python3 /home/root/RX_FM_USRP_UDP.py
