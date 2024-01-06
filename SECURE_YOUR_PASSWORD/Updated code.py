# pip install cryptography

from crypography.fernet import Fernet

key = Fernet.generate_key()

text = input("Text: ")

encrypted = Fernet(key).encrypt(text.encode())

print(f"Encrypted: {encrypted}")
print(f"Original: {text}")
