#!/usr/bin/python3

from socket import *

host_port = ("127.0.0.1", 9999) # setting the connection

s = socket(AF_INET, SOCK_DGRAM, 0) # DGRAM is for UDP
s.bind(host_port)

msg = "This is a message from the client"
s.sendto(msg.encode('ascii'), host_port) # encoding message

data, addr = s.recvfrom(1024)
print(data.decode('ascii'))

s.close()
