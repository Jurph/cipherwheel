# cipherwheel
Software implementation of the Field Notes cipher wheel that ships with "Clandestine" (Fall 2018) - see https://fieldnotesbrand.com/products/clandestine for details. 

The cipher wheel is a two-rotor wheel that places half of the alphabet on one rotor and half of the alphabet on the other rotor, alternating letters. While it is more complex than a straight one-direction shift (like ROT13) it is still a static alphabet that can be attacked with frequency analysis.  One other consequence of this design is that pairs of adjacent keys can create identical outputs. The two rotors in the default configuration generate a null offset with keys `XW` or `XV` -- that is, with either of those keys, "A" becomes "A" and so on.  

The alphabet in use is 36 characters (A-Z and 0-9) which easily accommodates 2,3,4,6, or 9 rotors. This project will, by default, support `cipherwheel.encode(plaintext, two_letter_key)` and `cipherwheel.decode(ciphertext, two_letter_key)` using the Field Notes rotor set. I'm also looking at specifying a `rotors.txt` file for specifying the number of rotors and a null cipher key (e.g. "3, ZOG") or taking a command-line argument `-r 3,ZOG`. 

TODO: define `encode()` and `decode()` functions.   
TODO: define `main()` with test output for the `XW` and `XV` null keys to verify functionality.  



