from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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
    
def add(p: tuple, q: tuple, a: int, mod: int) -> tuple:
    x1, y1 = p
    x2, y2 = q
    zero = (0, 0)
    k: int
    if p == zero:
        return q
    if q == zero:
        return p
    if x1 == x2 and y1 == -y2:
        return zero
    if p != q:
        k = (y2 - y1) * pow(x2 - x1, -1, mod)
    else:
        k = (3 * x1 * x1 + a) * pow(2 * y1, -1, mod)
    x3 = k * k - x1 - x2
    y3 = k * (x1 - x3) - y1
    x3 %= mod
    y3 %= mod
    return (x3, y3)

def times(x: tuple, n: int, a: int, mod: int) -> tuple:
    ret = (0, 0)
    while n:
        if n & 1:
            ret = add(ret, x, a, mod)
        x = add(x, x, a, mod)
        n >>= 1
    return ret

a = 497
b = 1768
p = 9739

q_x = 4726
q_y = pow(q_x ** 3 + a * q_x + b, (p + 1) // 4, p)
P = (q_x, q_y)
nb = 6534
shared_secret = times(P, nb, a, p)[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))