from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

"""
Encryption and decryption custom data using AES CBC Mode
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html?fbclid=IwAR2xK1EinalNCyOCEDsud7PFxA0Gqpxc3eGr0GegEYsCWaGeyiLlDGJuges

Script uses
    - master password (as a key for encryption and decryption)
    - 'fixed' IV (Initialization Vector) - hardcoded as empty string, can be fullfilled with data, but must be equal for one message to encrypt and decrypt
"""

#data = b'mysecretmessage'
#key=b'myultrasecretmasterkey'
iv = pad(b'', AES.block_size)

# data encryption
def encrypt_data(private_text, key):
    try:
        key_padded = pad(key, AES.block_size)
        cipher = AES.new(key_padded, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(private_text, AES.block_size))
        ct = b64encode(ct_bytes).decode('utf-8')
        return ct
    except Exception as e:
        print('Error during encryption occured: {0}'.format(e))

# data decryption
def decrypt_data(encrypted_message, key):
    try:
        key_padded_decrypted = pad(key, AES.block_size)
        ct_decrypted = b64decode(encrypted_message)
        cipher_decrypted = AES.new(key_padded_decrypted, AES.MODE_CBC, iv)
        decrypted_message = cipher_decrypted.decrypt(ct_decrypted)
        pt = unpad(decrypted_message, AES.block_size)
        return pt
    except Exception as e:
        print('Error during decryption occured: {0}'.format(e))


if __name__ == '__main__':
    print('hello, program started')
    data_to_encrypt = input('pass the string to encrypt ')
    password = input('pass the master password ')

    data_bytes = data_to_encrypt.encode('utf-8')
    password_bytes = password.encode('utf-8')

    encrypted_data = encrypt_data(data_bytes, password_bytes)
    print('Data to encrypt: {0}, encrypted data: {1}'.format(data_bytes, encrypted_data))

    decrypted_data = decrypt_data(encrypted_data, password_bytes)
    print('Decrypted data: {0}'.format(decrypted_data))