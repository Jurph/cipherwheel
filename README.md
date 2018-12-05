# cipherwheel
Software implementation of the Field Notes cipher wheel that ships with "Clandestine" (Fall 2018) - see https://fieldnotesbrand.com/products/clandestine for details. 

The cipher wheel is a two-rotor wheel that places half of the alphabet on one rotor and half of the alphabet on the other rotor, alternating letters. While it is more complex than a straight one-direction shift (like ROT13) it is still a static alphabet that can be attacked with frequency analysis. One other consequence of this design is that pairs of adjacent keys can create identical outputs - so instead of 36 x 36 possible unique keys, there are 36 x 18. The two rotors in the default configuration generate a null offset with keys `XW` or `XV` -- that is, with either of those keys, "A" becomes "A", "B" becomes "B", and so on.  

I implement the Field Notes cipher wheel specifically, making use of R. Ballestrini's code (https://russell.ballestrini.net/monoalphabetic-cipher-and-inverse-written-in-python/) for monoalphabetic shift ciphers but replacing the random alphabet with the Field Notes double-shifted version. The rotors are hard-coded but can be altered to support your own efforts. 

# security 

This is a monoalphabetic substitution cipher, which is a toy cipher. It is **not adequate** for protecting secrets with real-world consequences. This is adequate for protecting television spoilers, riddles, and any other puzzle that can be solved by a high school student with fewer than ~4 hours of effort. 
