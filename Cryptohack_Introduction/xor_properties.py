from pwn import *

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2_key1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_key3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_key1_key2_key3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key2 = xor(b'%s!' % bytes.fromhex(key2_key1), b"%s!" % bytes.fromhex(key1))
key3 = xor(b'%s!' % bytes.fromhex(key2_key3), b"%s!" % key2)
key1_key2_key3 = xor(b'%s!' % bytes.fromhex(key2_key3), b"%s!" % bytes.fromhex(key1))
flag = xor(b'%s!' % bytes.fromhex(flag_key1_key2_key3), b"%s!" % key1_key2_key3)
print(flag)
