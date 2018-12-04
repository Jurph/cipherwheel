from string import ascii_uppercase, digits
from random import shuffle

# Constants
alphabet = list(ascii_uppercase + digits)  # Defines a zero-indexed list [A-Z,0-9]

def addoffset(plainchar, offset_int):
    shiftedchar = alphabet[(alphabet.index(plainchar) + offset_int)%36]
    return shiftedchar


def makealphabet(key):
    # We make an alphabet by splitting the alphabet into lists of characters, dividing the
    # 36-character set into 1, 2, 3, or 4 rotors. Then we use the rotor_N_offset to shift
    # those letters based on the rotor's built-in offsets (hard-coded here). Then we use the
    # message key to apply further offsets to the alphabet subsets. Once we have a final offset
    # for each character we return a list of 36 offsets that can be applied to each character.
    keylength = int(len(key))
    rotors = [13, 35, 17, 3]
    rotor_settings = [0] * 36
    # With two rotors, modulo is always 0 or 1
    for letter in range(0, 36):
        if letter%keylength == 0:
            rotor_settings[letter] = addoffset(alphabet[letter], (rotors[0] + alphabet.index(key[0])))
        elif letter%keylength == 1:
            rotor_settings[letter] = addoffset(alphabet[letter], (rotors[1] + alphabet.index(key[1])))
        elif letter%keylength == 2:
            rotor_settings[letter] = addoffset(alphabet[letter], rotors[2] + alphabet.index(key[2]))
        elif letter%keylength == 3:
            rotor_settings[letter] = addoffset(alphabet[letter], rotors[3] + alphabet.index(key[3]))
        else:
            print("This system only supports 1-4 rotors")
            exit(1)
    return rotor_settings


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
    print("This should look like an all-caps alphabet: \n")
    newsetting = makealphabet("XB")
    print(newsetting)
