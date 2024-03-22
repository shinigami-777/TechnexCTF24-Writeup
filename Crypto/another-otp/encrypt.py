with open("./text.txt") as f: s = f.readlines()

from pwn import xor 

from os import urandom 

key = urandom(100)

encrypted = []

for i in s: encrypted.append(xor(i.strip().encode(), key))

with open("./output.txt", "w") as f:
    for i in encrypted: f.write(f'{i}\n')
