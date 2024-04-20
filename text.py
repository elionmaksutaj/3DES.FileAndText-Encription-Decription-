from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import binascii

while True:
     try:
       key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        print("Generated key has incorrect parity. Generating a new key...")

def encrypt(msg):
     cipher = DES3.new(key, DES3.MODE_EAX)
     nonce = cipher.nonce
     ciphertext = cipher.encrypt(msg.encode('ascii'))