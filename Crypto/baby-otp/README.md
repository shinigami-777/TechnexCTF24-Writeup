# baby otp
## Author : rasimhankunrava

### Description
Just your run of the mill One-Time-Pad. Should be unbreakable

### Attachments
[chall.py](chall.py)
```py
from secret import flag, key
assert type(flag) == bytes
assert type(key) == bytes
def xor(a,b):
    s = [bytearray(s) for s in (a,b)]
    xorrd = []
    for i in range(max(len(s[0]), len(s[1]))):
        xorrd.append(
            s[0][i%len(s[0])] ^ s[1][i%len(s[1])]
        )
    return bytes(xorrd)
print(xor(flag, key).hex())
# Output:
# 315110010b510b2a3172081055412c1a0d040658016b015a08071e0b56462c1d0d072c0f090014360304010451400e
```

### Solution
Since it is known that the flag must begin with `TechnexCTF{`, let's try to determine the first few bytes of the key:
```py
xbytes = bytes.fromhex('315110010b510b2a3172081055412c1a0d040658016b015a08071e0b56462c1d0d072c0f090014360304010451400e')  
prefix = b'TechnexCTF{'  
for i in range(len(prefix)):  
print(xbytes[i]^prefix[i], end=' ')
```
Output: `101 52 115 105 101 52 115 105 101 52 115`

It looks like `key` is simply `bytes([101, 52, 115, 105])`. Writing  the solve script:
```py
xorred_flag = bytes.fromhex('315110010b510b2a3172081055412c1a0d040658016b015a08071e0b56462c1d0d072c0f090014360304010451400e')
key = bytes([101, 52, 115, 105])
def xor(a,b):
    s = [bytearray(s) for s in (a,b)]
    xorrd = []
    for i in range(max(len(s[0]), len(s[1]))):
        xorrd.append(
            s[0][i%len(s[0])] ^ s[1][i%len(s[1])]
        )
    return bytes(xorrd)

print(xor(xorred_flag, key).decode('utf-8'))
# Output:
# TechnexCTF{y0u_sh0u1d_r3m3mb3r_th3_fl4g_f0rm4t}
```
#### Flag: `TechnexCTF{y0u_sh0u1d_r3m3mb3r_th3_fl4g_f0rm4t}`

