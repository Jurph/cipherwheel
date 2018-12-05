#!/usr/bin/python3
from string import ascii_uppercase, digits
from random import shuffle

# Constants
alphabet = list(ascii_uppercase + digits)  # Defines a zero-indexed list [A-Z,0-9]

def addoffset(plainchar, offset_int):
    shiftedchar = alphabet[(alphabet.index(plainchar) + offset_int)%36]
    return shiftedchar


def rotate(string, int):
    newstring = string[int:] + string[:int]
    return newstring


def makealphabet(key):

    # We make an alphabet by splitting the alphabet into lists of characters, dividing the
    # 36-character set into 1, 2, 3, or 4 rotors. We use the array of rotor offsets to shift
    # those letters to their "AA" configuration. This simulates the hardware configuration of
    # our two-rotor cipher wheel at "0,0". (There are 36x18 possibilities and rotors[] chooses ours.)
    # Once we have our hardware offsets, we simulate turning the rotors - that is, applying the
    # keys - the same way our wheel does. The first letter of the key determines the offset of
    # the plaintext letter "A" from the ciphertext letter "A": a classic Caesar Cipher offset (ROT36)
    # where knowing the shift value gives you all other letters. The second letter applies a relative
    # shift to the "demi-alphabet", moving "B" in the plaintext relative to "A" in the plaintext
    # so instead of +1 it will be at +3, +5, and so on up to +35 (or -1).

    rotors = [9, 13, 1, 2]   # Configure the hardware rotors (choose your own keys w/ you and your friends)

    keylength = int(len(key))  # Configure the "software" rotors - that is, the per-message key you're using

    key_turns = []
    for letter in key:
        key_turns.append(alphabet.index(letter))
    print("For key {} the key turns are:\n{}".format(key, key_turns))

    str_alphabet = ascii_uppercase + digits

    # Shift the demi-alphabets relative to one another
    evens = ""
    odds = ""
    for letter in str_alphabet:
        if str_alphabet.index(letter)%keylength == 0:
            evens += letter
        else:
            odds += letter

    # Apply secondary rotor and secondary key digit
    odds = rotate(odds, rotors[1] + key_turns[1])
    # Shuffle the evens and odds back into an alphabet
    demi_shift = ""
    for letter in odds:
        demi_shift += evens[odds.index(letter)]
        demi_shift += odds[odds.index(letter)]

    # Rotate the whole alphabet using the primary rotor and first key digit
    whole_shift = list(rotate(demi_shift, (rotors[0] + key_turns[0])))
    print(whole_shift)
    return whole_shift


#  (RB) These functions from R. Ballestrini
def random_monoalpha_cipher(pool=None):
    """Generates a Monoalphabetic Cipher as a dictionary"""
    if pool is None:
        pool = ascii_uppercase + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))


def inverse_monoalpha_cipher(monoalpha_cipher):
    """Given a Monoalphabetic Cipher (dictionary) return the inverse."""
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.iteritems():
        inverse_monoalpha[value] = key
    return inverse_monoalpha


def encrypt_with_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)


def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    return encrypt_with_monoalpha(
               encrypted_message,
               inverse_monoalpha_cipher(monoalpha_cipher)
           )


if __name__ == "__main__":
    # Just run unit tests if run standalone
    print("Unit tests for incrementing A, Z, 0, and 9 by 7.")
    print(addoffset("A", 7))
    print(addoffset("Z", 7))
    print(addoffset("0", 7))
    print(addoffset("9", 7))
    print("This should look like the alphabet shifted 12 slots:")
    print(rotate(alphabet, 12))
    print("Using key 'XW' this should look like an all-caps alphabet:")
    newsetting = makealphabet("XW")
    # print(newsetting)
    print("Using key 'XV' this should look like an all-caps alphabet:")
    newsetting = makealphabet("XV")
    # print(newsetting)
    print("Using key 'AA' this should look like an all-caps mixed alphabet starting '1 O 3 Q 5 S 7...':")
    newsetting = makealphabet("AA")
    # print(newsetting)