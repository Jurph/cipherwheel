import string

def encrypt(plaintext, key):
    ciphertext = plaintext
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ciphertext
    return plaintext

def makealphabet(key):
    rotor_1_offset = 24  # When [key1] is 24 (X) the odd slots are null.
    rotor_2_offset = 34  # When [key1] - [key2] is -2 (or -3) the even slots are null.
    rotor_3_offset = 14  # Not used yet
    rotor_4_offset = 4   # Not used yet
    alphabet = list(map(chr, range(48, 57))) + list(map(chr,range(65, 90)))
    keylength = int(len(key))