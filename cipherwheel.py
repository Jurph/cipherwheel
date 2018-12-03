import string

def encrypt(plaintext, key):
    ciphertext = plaintext
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ciphertext
    return plaintext

def makealphabet(key):
    # We make an alphabet by splitting the alphabet into lists of characters, dividing the
    # 36-character set into 1, 2, 3, or 4 rotors. Then we use the rotor_N_offset to shift
    # those letters based on the rotor's built-in offsets (hard-coded here). Then we use the
    # message key to apply further offsets to the alphabet subsets. Once we have a final offset
    # for each character we return a list of 36 offsets that can be applied to each character.
    keylength = int(len(key))
    rotor_1_offset = 24  # When [key1] is 24 (X) the odd slots are null.
    rotor_2_offset = 34  # When [key1] - [key2] is -2 (or -3) the even slots are null.
    rotor_3_offset = 14  # Not used yet
    rotor_4_offset = 4   # Not used yet
    alphabet = list(map(chr, range(48, 57))) + list(map(chr,range(65, 90)))
    return alphabet

