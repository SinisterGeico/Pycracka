# Pycracka v1.0
# Made By Alex Haug
- Please credit me if using for anything besides private use
- I am not liable for anything you do with this software.
- I am new to coding so any suggestions/optimizations appreciated.

# hashgenerator.py 
- creates a hash for any input. It does not do salt.
- Creates hashes in:
- MD-5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512

# Pycracka.py
- it is the engine that powers pycracka_app.py
- cannot be in the same directory as pycracka_app.py

# Pycracka_app.py
- This is the thing you actually run.
- Capable of cracking all hashes that hashgenerator.py can create
- uses a very simple bruteforce algorithm to iterate through all combinations of a given character set/sets. 
- supports uppercase, lowercase, and digits
- DOES NOT SUPPORT SALT

# CONCLUSION/INFO
made for my computer science 10 final project

modules used:
- termcolor
- hashlib
- itertools

sources
- https://repl.it/@CyanCoding/Brute-Force-Password-Cracker
- https://github.com/Starwarsfan2099/Python-Hash-Cracker
- https://www.pythoncentral.io/hashing-strings-with-python/

built in Pycharm CE 2019.2.3
