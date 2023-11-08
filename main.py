from cryptography.fernet import Fernet

def get_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    f = Fernet(key)
    encripted_text = f.encrypt(text.encode())
    return encripted_text

def decrypt_text(encrypted_text, key):
    f =  Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode()
    return decrypted_text

#Generate a secret key
secret_key = get_key()

# Text to be encrypted
original_text = "Este es un mensaje ultrasecreto."
print("*"*100)
print(f"Original text: {original_text}")
print("*"*100)

# Encrypt text
secret_text = encrypt_text(original_text, secret_key)
print(f"Encrypted text: {secret_text}")
print("*"*100)

# Decrypt text
decoded_text = decrypt_text(secret_text, secret_key)
print(f"Decrypted text: {decoded_text}")
print("*"*100)