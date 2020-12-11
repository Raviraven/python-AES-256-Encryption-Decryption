# Simple AES encryption and description script
Simple script written for learning basics of string encryption / decryption in python

## How does it work?
Script, when running - asks user for the string to encrypt and master password, which will be used as key.  

Then script run two functions:  
1. Encryption (result will be printed in console)  
2. Decryption (the same situation - result in console)

For both functions the same IV is used - generated with blank characters (this can be changed, but remember - you have to use **the same IVs** for encryption and decryption!)

## Setup
1. Download repository
2. Install required packages
```
pip install -r requirements.txt
```
3. Run script using terminal
```
python "AES CBC_mode.py"
```
4. Start using script 😊

## Urls
1. [PyCryptodome documentation](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html?fbclid=IwAR2xK1EinalNCyOCEDsud7PFxA0Gqpxc3eGr0GegEYsCWaGeyiLlDGJuges)
