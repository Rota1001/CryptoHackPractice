from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

n = []
e = []
c = []
for i in range(1, 51):
    with open(f'keys_and_messages/{i}.pem', "rb") as f:
        key = RSA.importKey(f.read())
        n.append(key.n)
        e.append(key.e)
    with open(f'keys_and_messages/{i}.ciphertext', "rb") as f:
        c.append(bytes.fromhex(f.read().decode()))

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] != n[j] and GCD(n[i], n[j]) != 1:
            p = GCD(n[i], n[j])
            q = n[i] // p
            phi = (p - 1) * (q - 1)
            d = pow(e[i], -1, phi)
            key = RSA.construct((n[i], e[i], d))
            cipher = PKCS1_OAEP.new(key)
            m = cipher.decrypt(c[i])
            print(m)


