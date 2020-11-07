import socket
import time
import sys


if len(sys.argv) < 3:
    print("usage: \"python fuzz.py [host] [port]\"")
    exit(0)


host = sys.argv[1]
port = sys.argv[2]
size = 100

while size < 10000:

    try:
        inputBuffer = "A" * size
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print("Trying " + str(size) + " bytes")
        s.send(inputBuffer)
        s.recv(1024)
        s.close()
    
        size += 100
        time.sleep(10)
    except:
        print("died at " + str(size - 100) + " bytes")
        exit(0)



