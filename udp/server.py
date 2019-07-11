#!/usr/bin/python3

from socket import *

host_port = ("127.0.0.1", 9999) # setting the host on port (in exec is an arbitrary port number)

s = socket(AF_INET, SOCK_DGRAM) # UDP sock
s.bind(host_port) # creating connections

while(True):

    data, addr = s.recvfrom(1024) # receiving from method -> data is the message streamed
    print("Got connection from: ", addr)
    print(data.decode('ascii')) # printed and decoded

    # sending message to client
    msg = "This is a message from the server"
    s.sendto(msg.encode('ascii'), addr)
    break

s.close()
