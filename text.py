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
    print("Zgjedhe një opsion:")
    print("1. Enkriptim")
    print("2. Dekriptim")
    choice = input("Shtyp zgjedhjen tuaj (1 or 2): ")
    if choice == '1':
        plaintext = input('Shtyp plaintext: ')
        nonce, ciphertext = encrypt(plaintext)
        print('Nonce:', binascii.hexlify(nonce).decode('ascii'))
        print('Cipher text:', ciphertext.hex())
    elif choice == '2':
        ciphertext = bytes.fromhex(input('Shtyp ciphertext në formatin  hex: '))
        nonce = binascii.unhexlify(input('Shtyp nonce në formatin hex: '))
        plaintext = decrypt(nonce, ciphertext)
        print('Decrypted text:', plaintext)
     else:
        print("Zgjedhje e pasaktë. Të lutem shtyp 1 ose 2.")

        again = input("Dëshiron të performon një operacion tjetër? (po/jo): ")
    if again.lower() != 'yes':
        break
