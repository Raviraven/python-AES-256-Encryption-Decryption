from cryptography.fernet import Fernet

# fernet encyption in python: https://nitratine.net/blog/post/encryption-and-decryption-in-python/

def generate_key():
    return Fernet.generate_key()


# function returns encrypted message as bytes
def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


# function receives message as bytes
# returns decrypted message as string
def decrypt_message(message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(message)
    return decrypted_message.decode()
