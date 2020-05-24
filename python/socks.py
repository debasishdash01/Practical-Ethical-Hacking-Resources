#!/usr/bin/env python

import socket

host = '127.0.0.1'
port = 4445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host,port)

#Think of AF_INET as IP address
#Think of SOCK_STREAM as a Port
#This will just make a connection, after that it will quickly terminate as we didnt tell it to be persistent.
