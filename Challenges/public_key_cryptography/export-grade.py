from math import ceil, sqrt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from tqdm import tqdm


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


def bsgs(g, y, p):
    m = int(ceil(sqrt(p - 1)))
    S = {pow(g, j, p): j for j in tqdm(range(m))}
    gs = pow(g, p - 1 - m, p)
    for i in tqdm(range(m)):
        if y in S:
            return i * m + S[y]
        y = y * gs % p
    return None

p = 0xde26ab651b92a129
g = 0x2
A = 0x99a2a6b232db5a9c
# print(g)
# print(A)
# print(p)
# print(p - 1)
k = 2
print(pow(2,  (p - 1) // 2 , p))
# a = bsgs(g, A, p)
# print(a)
# B = 0x6d6b69259dfaa9b0
# shared_secret = pow(B, a, p)
# iv = "b1e28d2c0f7c0527a4d32c5a053de05c"
# encrypted_flag = "6b1e2ddfde104f4f6bae44b41703695cd3ac7bfa735fcc3b8a4065eab52a3982"


# print(decrypt_flag(shared_secret, iv, encrypted_flag))