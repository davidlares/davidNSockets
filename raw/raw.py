#!/usr/bin/python3

from socket import *

host = "127.0.0.1" # setting the connection

s = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
# where AF_INET is the type of addresses that socket can communicate with = IPv4\
# IPPROTO_ICMP -> No protocol, use the default

s.bind((host,0))

# configuring the socket
s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1) # proto IP, and HDRINCL for information, 1 is for tuning on

# printing
print(s.recvfrom(65565))
