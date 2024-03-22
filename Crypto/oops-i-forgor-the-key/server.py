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
