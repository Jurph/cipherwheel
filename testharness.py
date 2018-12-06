#!/usr/bin/python3
from string import ascii_uppercase, digits
import cipherwheel

keyspace = ascii_uppercase + digits

for item1 in keyspace:
    for item2 in keyspace:
        testkey = item1 + item2
        if cipherwheel.makealphabet(testkey) == cipherwheel.makealphabet("XW"):
            print("Found possible null cipher at key {}".format(testkey))
        else:
            next = 1

