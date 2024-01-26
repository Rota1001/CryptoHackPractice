from Crypto.Cipher import AES
import hashlib
import random

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

with open("./Challenges/SymmetricCryptography/words", encoding="utf-8") as f:
    words = [w.strip() for w in f.readlines()]
for word in words:
    KEY = hashlib.md5(word.encode()).digest().hex()
    text = decrypt('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66', KEY)
    if text[0:5] == b"crypt":
        print(text)
        break

print(len(words))
#23167185f5c0719c529f094b6f0d3fc0
#23167185f5c0719c529f094b6f0d3fc0