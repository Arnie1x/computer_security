# Write a function that takes two equal-length buffers and produces their XOR combination.

from pwn import *

val = '1c0111001f010100061a024b53535009181c'
val2 = '686974207468652062756c6c277320657965'

result = xor(b'%s!' % bytes.fromhex(val), b"%s!" % bytes.fromhex(val2)).removesuffix(b'\x00')

print(result)
print(bytes.hex(result))
