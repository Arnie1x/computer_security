def repeated_key_xor(plain_text, key):
    # returns plain text by repeatedly xor-ing it with key
    pt = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)


def main():
    plain_text = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = b'ICE'

    print("Plain text: ", plain_text)
    print("Encrypted as: ", repeated_key_xor(plain_text, key).hex())


if __name__ == '__main__':
    main()
