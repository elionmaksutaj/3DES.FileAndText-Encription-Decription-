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
     return nonce, ciphertext

def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
     return plaintext.decode('ascii')

while True:
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        plaintext = input('Enter plaintext: ')
        nonce, ciphertext = encrypt(plaintext)
        print('Nonce:', binascii.hexlify(nonce).decode('ascii'))
        print('Cipher text:', ciphertext.hex())
    elif choice == '1':
        ciphertext = bytes.fromhex(input('Enter ciphertext in hex format: '))
