#!/usr/bin/python

import socket
import time
import sys


if len(sys.argv) < 3:
    print("usage: \"./fuzz.py [target] [port] [cmd]\"")
    exit(0)

target = sys.argv[1]
port = int(sys.argv[2])
size = 100
if len(sys.argv) == 4:
    cmd = sys.argv[3] + " "
else:
    cmd = ""

cmd = cmd.lstrip(" ")


while size < 10000:

    try:
        inputBuffer = cmd + "A" * (size - len(cmd))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.send(inputBuffer)
        s.recv(1024)
        s.close() 

        if(size != 100):
            print("buffer size of " + str(size - 100) + " bytes OK")
        
        size += 100
        time.sleep(3)
    except:
        print("died at " + str(size - 100) + " bytes")
        exit(0)

