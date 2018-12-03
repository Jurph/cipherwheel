import string

# Constants
alphabet = list(map(chr,range(65, 91))) + list(map(chr, range(48, 58)))  # Defines a zero-indexed list [A-Z,0-9]


# Functions
def encrypt(plaintext, key):
    newalphabet = makealphabet(key)
    ciphertext = map(plaintext.upper(), newalphabet)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ciphertext.upper()
    return plaintext


def addoffset(plainchar, keyletter):
    offset = (ord(str(plainchar)) + ord(str(keyletter)))%36
    shiftedchar = alphabet[offset]
    return shiftedchar


def makealphabet(key):
    # We make an alphabet by splitting the alphabet into lists of characters, dividing the
    # 36-character set into 1, 2, 3, or 4 rotors. Then we use the rotor_N_offset to shift
    # those letters based on the rotor's built-in offsets (hard-coded here). Then we use the
    # message key to apply further offsets to the alphabet subsets. Once we have a final offset
    # for each character we return a list of 36 offsets that can be applied to each character.
    keylength = int(len(key))

    # TODO: put these in an array so I can condense the keying IF/ELSE below
    rotor_1_offset = 24  # When [key1] is 24 (X) the odd slots are null.
    rotor_2_offset = 34  # When [key1] - [key2] is -2 (or -3) the even slots are null.
    rotor_3_offset = 14  # Not used yet
    rotor_4_offset = 4   # Not used yet
    newalphabet = list()
    for letter in range(1, 36):
        if letter%keylength == 0:
            newalphabet[letter] = addoffset(alphabet[letter], rotor_1_offset)
        elif letter%keylength == 1:
            newalphabet[letter] = addoffset(alphabet[letter], rotor_2_offset)
        elif letter%keylength == 2:
            newalphabet[letter] = addoffset(alphabet[letter], rotor_3_offset)
        else:
            exit()
    return newalphabet


if __name__ == "__main__":
    plaintext = "tHiS iS a TEst 123 456"
    key = 'QZ'
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext using key {} is:\n {}".format(key, ciphertext))
    plaintext = decrypt(ciphertext, key)
    print("Plaintext using key {} is:\n {}".format(key, ciphertext))
