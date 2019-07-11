#!/usr/bin/python3
from socket import *

host = "127.0.0.1" # setting the connection
port = 9999

s = socket(AF_INET, SOCK_STREAM, 0) # setting up the same socket configuration
s.connect((host,port))

msg = "Hello, from the client"
s.send(msg.encode('ascii')) # sending an encoded message

rmsg = s.recv(1024) # server messasge received
print(rmsg.decode('ascii'))
s.close()
