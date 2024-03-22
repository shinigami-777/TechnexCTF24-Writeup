# another otp
## Author : rasimhankunrava

### Description

This time the One-Time Pad is even more secure. I even used `os.urandom()`. Good luck bruteforcing that.

### Attachments
- [encrypt.py](encrypt.py)
```py
with open("./text.txt") as f: s = f.readlines()
from pwn import xor 
from os import urandom 
key = urandom(100)
encrypted = []
for i in s: encrypted.append(xor(i.strip().encode(), key))
with open("./output.txt", "w") as f:
    for i in encrypted: f.write(f'{i}\n')
```
- [output.txt](output.txt)

### Solution
The solution is based on the assumption that each character in the unknown `text.txt` is printable (which turns out to be correct afterwards).

#### Approach
Consider the first byte of the first encrypted line. Let's xor it with each printable character one by one, and make a list of the results. Now, exactly one of the elements of the list is bound to be the first byte of the key (because exactly one of the printable characters is the first character of  the unknown plaintext file).
The above process is repeated with the first byte of each line, and the intersection of all the resulting lists is taken. Moreover, to reduce the number of possibilities even further, the 101th[, 201th and so on] byte of each line (if exists) is also made to go through the same process, thus reducing the number of possibilities even further.

The same process is repeated to 2nd, 102th, 202th (and so on) byte of each encrypted line, to get the possible second byte of the key.

Using all the ascii printable characters this way results in a large number of possible key combinations. I had to reduce the list of printable characters to just `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{} ` in order to get it down to just 32 possible key combinations, the first one of which resulted in the desired plaintext.
#### Solve script
[solution.py](solution/solution.py)
#### Flag: `TechnexCTF{reusing the key is weak stuff}`

