# utils/crypto.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import string

# AES Encryption / Decryption

def generate_key():
    """Generates a new AES encryption key using Fernet."""
    return Fernet.generate_key()

def encrypt_aes(text, key):
    """Encrypts text using AES (Fernet)"""
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text.decode()

def decrypt_aes(encrypted_text, key):
    """Decrypts AES encrypted text."""
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    return decrypted_text.decode()

# Caesar Cipher Encryption / Decryption

def caesar_encrypt(text, shift):
    """Encrypts text using Caesar Cipher."""
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    """Decrypts text using Caesar Cipher."""
    return caesar_encrypt(text, -shift)  # Reuse encryption with negative shift
