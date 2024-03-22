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




