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


p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
A = 0x355f02b806edf7ea6a5194b31458f5d544136edc4917c3ff0919259912a7b96c3327cd05a4ca3f70ea8722d99d6a65b6f4c39ccb393a4f571008b3e6e8d8f041955db3370ea7358ddfc00f26201a66dd416cbb0a8f54ac5aa0e485ed1d6d596763fbbca492f50d18f8a151bdd2af4d7bbfdad8f74e256ed22fa143699327aa2729556efa5ae5d1a1f981c270cda0f8558a822670ce062c85cf7820f36909d4c8cdcceff901d9f72237860b8ba3db7107d2c7ede7101d803b60ba13fcd599add9
shared_secret = A
iv = '372ea383ccbef0c9c423b53e34d9965d'
ciphertext = '4a087b0c67e99e4c534f57835b38c6ffb56f4e1268be95661fbc4bfa288b9cf5'

print(decrypt_flag(1, iv, ciphertext))
