# Buffer_Overflow_Scripts
A set of scripts I use for buffer overflows

**1. fuzz.py**

Helps begin the process by fuzzing the target
- the limit is currently set to 10000 but in some cases this may need to be increased
- When the fuzzer is unable to reach the target, it assumes the target crashed from the previous buffer sent

usage: `./fuzz.py [target ip] [target port]`

<hr>

**2. reproduce.py**

After causing a crash, it is important to verify that the crash is reproducable with the given amount
- otherwise it is unclear if this was a random crash or not

usage: `./reproduce.py [target ip] [target port] [buffer size]`

<hr>

**3. offset.py**

After knowing there is a consistent crash, now the exact offset can be located
- this requires the user inserts an offset pattern using `msf-pattern_create -l [size]`

usage: `./offset.py [target ip] [target port]`

<hr>

**4. target.py**

After locating the offset, to verify it is correct, the `target.py` script will try to nail the EIP value on the head
- if successful, the EIP value should be equal to "BBBB" at the time of crash

usage: `./target.py [target ip] [target port] [size] [eip]`

<hr>

**5. space.py**

After having control over the EIP value, it is time to find space for the exploit shellcode. 
- `space.py` will write indicators before and after the EIP value to see which registers reference these locations

`space.py` also has a secondary usage of locating jmp commands for registers that may be relevant 
- some register are much more likely to be relevant than others
- these values were found through `msf-nasm_shell`, I just found it easier to grab them from the python script directly

usage #1: `./space.py [target ip] [target port] [size] [eip]`</br>
usage #2: `./space.py [register name]`

<hr>

**6. badchars.py**

Now comes the task of finding bad characters
- the script will send all hex characters along with the length needed to crash the target
- "\x00" is omitted as it is always a bad character

usage: `./badchars.py [target ip] [target port] [size]`

<hr>

**7. jump.py**

Before inserting shellcode, this script can target the jump address to verify the execution flow will jump to the correct location
- make sure to set a breakpoint at the target JMP instruction
- the 'ret' variable must be changed within the script to the corresponding jump location
- `jump.py` can also convert a return address (ex. `1234ABCD`) into little endian (ex. `\xcd\xab\x34\x12`)

usage #1: `./jump.py [target ip] [target port] [size] [eip]`
usage #2: `./jump.py [return adderss]`

<hr>

**8. exploit.py**

Finally the exploit script for the shellcode
- the order of the final buffer may change based on where space is available
- make sure to note the size of the shellcode from msfvenom!`
- a NOP sled of 32 is included but may need to change depending on the exploit
- the 'ret' variable must be changed within the script to the corresponding jump location
- `exploit.py` can also convert a return address (ex. `1234ABCD`) into little endian (ex. `\xcd\xab\x34\x12`)

usage #1: `./exploit.py [target ip] [target port] [size] [eip]`
usage #2: `./exploit.py [return adderss]`

<hr>

**charlist.py**

In case you don't have a copy of all the hex characters, this will generate them quickly for you

usage: `python charlist.py`

