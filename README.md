# What Index of Coincidence ?
- The coincidence index is an indicator used in cryptanalysis which makes it possible to evaluate the global distribution of letters in encrypted message for a given alphabet.

# How to use Index of Coincidence ?
- For a given ciphered message, the value for the index of coincidence allows to filter the list of ciphering methods to use. It is one of the first cryptanalysis technique.
- If the Index of coincidence is high (close to 0.070), i.e. similar to plain text, then the message has probably been crypted using a transposition cipher (letters were shuffled) or a monoalphabetic substitution (a letter can be replaced by only one other).

- If the Index of coincidence is low (close to 0.0385), i.e. similar to a random text, then the message has probably been crypted using a polyalphabetic cipher (a letter can be replaced by multiple other ones).

 - The more the coincidence count is low, the more alphabets have been used.
 - Example: Vigenere cipher with a key of length 4 to 8 letters have an IC of about 0.045 ± 0.05

# Usage 
```
python IC.py cipher_file
```
