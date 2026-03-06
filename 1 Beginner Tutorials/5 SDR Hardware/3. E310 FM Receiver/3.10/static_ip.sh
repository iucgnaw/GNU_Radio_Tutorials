#!/bin/sh

# 1. Flush existing IP addresses
ip addr flush dev eth0

# 2. Assign static IP and netmask
ip addr add 10.67.44.142/24 dev eth0

# 3. Bring the interface up
ip link set eth0 up

# 4. Add default gateway
ip route add default via 10.0.0.1
