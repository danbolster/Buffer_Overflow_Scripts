from __future__ import print_function

for i in range(1,256):
    print("\\x" + "{:02x}".format(i), end='')

print()
