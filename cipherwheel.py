#!/usr/bin/python3
from string import ascii_uppercase, digits
from random import shuffle
import unittest


# Simple Functions
def addoffset(plainchar, offset_int):
    alphabet = list(ascii_uppercase + digits)  # Defines a zero-indexed list [A-Z,0-9]
    shiftedchar = alphabet[(alphabet.index(plainchar) + offset_int)%36]
    return shiftedchar


def rotate(string, int):
    newstring = string[int:] + string[:int]
    return newstring


def makealphabet(key):

    # We make a new alphabet by splitting the alphabet into lists of characters, dividing the
    # 36-character set across N (currently 2) rotors. We use the array of rotor offsets to shift
    # those letters to their "AA" configuration. This simulates the hardware configuration of
    # our two-rotor cipher wheel at "0,0". (There are 36x18 possibilities and rotors[] chooses ours.)
    # Once we have our hardware offsets, we simulate turning the rotors - that is, applying the
    # keys - the same way our wheel does. The first letter of the key determines the offset of
    # the plaintext letter "A" from the ciphertext letter "A": a classic Caesar Cipher offset (ROT36)
    # where knowing the shift value gives you all other letters. The second letter applies a relative
    # shift to the "demi-alphabet", moving "B" in the plaintext relative to "A" in the plaintext
    # so instead of +1 it will be at +3, +5, and so on up to +35 (or -1).

    str_alphabet = ascii_uppercase + digits  # Start with our 36-char alphabet
    rotors = [13, 13, 1, 2]   # Configure the hardware rotors (choose your own keys w/ you and your friends)
    keylength = int(len(key))  # Configure the "software" rotors - that is, the per-message key you're using
    key_turns = []
    for letter in key:
        key_turns.append(str_alphabet.index(letter))
    # print("For key {} the key turns are:\n{}".format(key, key_turns))

    # Create demi-alphabets and shift one relative to the other
    evens = ""
    odds = ""
    for letter in str_alphabet:
        if str_alphabet.index(letter)%keylength == 0:
            evens += letter
        else:
            odds += letter

    # Apply secondary rotor and second key digit
    demi_rotation = int((rotors[1] + key_turns[1])/2)+1
    odds = rotate(odds, demi_rotation)
    # print("Rotated demi-alphabet by {}".format(demi_rotation))

    # Shuffle the evens and odds back into an alphabet
    demi_shift = ""
    for letter in odds:
        demi_shift += evens[odds.index(letter)]
        demi_shift += odds[odds.index(letter)]
    # print("Reshuffled alphabet now reads {}".format(demi_shift))

    # Rotate the whole alphabet using the primary rotor and first key digit
    whole_shift = list(rotate(demi_shift, (rotors[0] + key_turns[0])))
    # print(whole_shift)
    return whole_shift


def keyed_wheel_cipher(key, pool=None):
    """Generates a monoalphabetic cipher dict from a cipher wheel"""
    if pool is None:
        pool = ascii_uppercase + digits
    original_pool = list(pool)
    shuffled_pool = makealphabet(key)
    return dict(zip(shuffled_pool, original_pool))


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
    for key, value in monoalpha_cipher.items():         # changed "iteritems" to "items" for Python 3.x compatibility
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


class TestCustomFunctions(unittest.TestCase):

    def test_offset(self):                              # Tests addoffset(str, int)
        self.assertEqual(addoffset('B', 0), 'B')        # Does nothing when it should
        self.assertEqual(addoffset('B', 7), 'I')        # Does what it ought to
        self.assertEqual(addoffset('9', 7), 'G')        # Wrap around correctly
        self.assertEqual(addoffset('G', -10), '6')      # Wrap around wrong direction
        self.assertEqual(addoffset('Z', 10), '9')       # Letter/number crossing


    def test_rotate(self):
        self.assertEqual(rotate('ZAGNUT', 0), 'ZAGNUT')     # Do nothing
        self.assertEqual(rotate('DONGTAR', 4), 'TARDONG')   # Rotate forward
        self.assertEqual(rotate('SHATNER', -3), 'NERSHAT')  # Rotate backward
        # TODO: Learn syntax for assertRaises() so I can prove e.g. rotate('DOG','cat') fails

    def test_create_rotors(self):
        self.assertListEqual(makealphabet("XW"),
                         ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.assertListEqual(makealphabet("XW"), makealphabet("XV"))
        self.assertListEqual(makealphabet("AA"),
                         ['1', 'O', '3', 'Q', '5', 'S', '7', 'U', '9', 'W', 'B', 'Y', 'D', '0', 'F', '2', 'H', '4', 'J',
                          '6', 'L', '8', 'N', 'A', 'P', 'C', 'R', 'E', 'T', 'G', 'V', 'I', 'X', 'K', 'Z', 'M'])
        self.assertListEqual(makealphabet("FN"),
                            ['S', 'L', 'U', 'N', 'W', 'P', 'Y', 'R', '0', 'T', '2', 'V', '4', 'X', '6', 'Z', '8', '1',
                              'A', '3', 'C', '5', 'E', '7', 'G', '9', 'I', 'B', 'K', 'D', 'M', 'F', 'O', 'H', 'Q', 'J'])

    def test_encryption(self):
        eff_enn = keyed_wheel_cipher("FN")
        self.assertEqual(encrypt_with_monoalpha('HELLO', eff_enn), '7WBB6')
        self.assertEqual(decrypt_with_monoalpha('7WBB6', eff_enn), 'HELLO')


if __name__ == "__main__":
    unittest.main()


