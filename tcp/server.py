#!/usr/bin/python3

from socket import * #importing all

host = "127.0.0.1" # setting the host on port
port = 9999

# open the socket
s = socket(AF_INET, SOCK_STREAM, 0)

# where AF_INET is the type of addresses that socket can communicate with = IPv4
# SOCK_STREAM - Connection based protocol -> TCP
# third param: 0 (default protocol)

s.bind((host,port)) # creating connections
s.listen(5) # number of connections

while(True):
    c, addr = s.accept() # accepting connections on the server
    rmsg = c.recv(1024) # received message on TCP connections, where 1024 is bufsize
    print(rmsg.decode('ascii')) # printing the received message decoding via ASCII

    msg = "This is a message for the server"
    c.send(msg.encode('ascii')) # sending message
    break

s.close()
