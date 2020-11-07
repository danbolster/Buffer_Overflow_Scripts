#!/usr/bin/python

import socket
import time
import sys

if len(sys.argv) < 4:
    print("usage: \"./reproduce.py [target] [port] [size]\"")
    exit(0)

target = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])

inputBuffer = "A" * size

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
s.close()
exit(0)     



