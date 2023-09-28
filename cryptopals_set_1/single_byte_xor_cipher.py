from pwn import *

data = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
dataHex = bytes.fromhex(data)


# Function to decrypt a message with a given key
def byte_xor(input_bytes, key):
    flag = b''
    for a in input_bytes:
        flag += bytes([a ^ key])
    return flag.decode('utf-8', errors='ignore')


most_spaces = 0
output = ''


# Function to count the spaces in a string to determine the character frequency
def check_spaces():
    global output, most_spaces
    # This loop is used to find the key used to encrypt the message
    for k in range(256):
        outcome = byte_xor(dataHex, k)
        no_of_spaces = outcome.count(' ')
        if no_of_spaces > most_spaces:
            most_spaces = no_of_spaces
            output = outcome
    return output


print(check_spaces())
