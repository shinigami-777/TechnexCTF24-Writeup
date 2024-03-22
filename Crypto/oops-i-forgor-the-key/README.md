# oops i forgor the key
## Author : rasimhankunrava

### Description
Hi, I will give you the flag, just ask me nicely.

What do you mean than you need the key to encrypt your message through AES ?

Anyways, manage somehow, I have a college fest to enjoy.

`nc ctf.technex.co.in 6900`

### Attachments
[server.py](server.py)
```py
#!/bin/python3
from Crypto.Cipher import AES
from secret import key, flag


def unpad(padded_data: bytes):
    pdata_len = len(padded_data)
    if pdata_len == 0: raise ValueError("empty message must be padded")
    if pdata_len % 16: raise ValueError("Input data is not padded")

    padding_len = padded_data[-1]

    if padding_len < 1 or padding_len > min(16, pdata_len):
        raise ValueError("Padding is incorrect.")
    if padded_data[-padding_len:] != bytes([padding_len]) * padding_len:
        raise ValueError("Padding is incorrect.")
    return padded_data[:-padding_len]


while True:
    try:
        iv = bytes.fromhex(input("iv: "))
        if len(iv) != 16: raise Exception
        msg = bytes.fromhex(input("encrypted message: "))
        if len(msg) % 16: raise Exception
    except:
        print("you broke something", flush=True)
        print("bai", flush=True)
        exit(0)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(msg)
    try:
        plaintext = unpad(plaintext)
    except:
        print("I didn't quite catch that, try again", flush=True)
        continue

    if plaintext == b"send flag pls":
        print(flag, flush=True)
        break
    else:
        print("I don't understand, try again", flush=True)
```

### Solution
This is based on a simple [padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack#Encrypting_messages_with_Padding_oracle_attack_(CBC-R)) on one block, using known plaintext.
Solve script:
```py
from pwn import *
p = remote('ctf.technex.co.in', 6900)
p.recvuntil(b'iv: ')
dec = b''
for bhak in range(16):
  print('over:', bhak, dec)
  for i in range(0xff):
    indexx = len(dec)
    payload = '00'*(16-indexx-1) + bytes([i]).hex()
    if indexx>0:
      payload+= xor(dec,indexx+1).hex()
    payload=payload.encode('ascii')
    print('payload:',len(payload), payload)
    p.sendline(payload)
    p.recvuntil(b'ge: ')
    p.sendline(b'00'*16)
    res=p.recvline()
    if b'understand' in res:
      print(i)
      dec = bytes([i^(indexx+1)]) + dec
      print('log:',dec)
      break
    print(i,'| ',end='')

# result:
assert (dec == b'\xacV_\xb1\xd2\xf0\x95\xa3\x94\x8c\xfd\xfb\x97\xa8\xea\x90')
fpt = b"send flag pls"
fpt+=bytes([16-len(fpt)])*(16-len(fpt))
payload=xor(dec,fpt)
p.sendline(payload.hex().encode())
p.recvuntil(b'ge: ')
p.sendline(b'00'*16)
print(p.recvline())
# output:
b'TechnexCTF{y0u_d1dn7_n33d_th3_k3y_OwO}\n'
```
#### Flag: `TechnexCTF{y0u_d1dn7_n33d_th3_k3y_OwO}`
