from pwn import *

data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
dataHex = bytes.fromhex(data)

def byte_XOR(input_bytes, key):
    flag = b''
    for a in input_bytes:
        flag += bytes([a ^ key])
    return flag.decode('utf-8')


for k in range(256):
    outcome = byte_XOR(dataHex, k)
    if 'crypto' in outcome:
        print(outcome)
        break
