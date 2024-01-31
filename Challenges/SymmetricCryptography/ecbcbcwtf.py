import os
import requests

def xor_byte(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

ciphertext = '8cd0a741c1912d399a94c0f7fd5288ac62b31b28a8017fa193aedf3604bb94f7f4b94bbd0315da19e0d584ff0ef2cdbe'
plaintext = requests.get("https://aes.cryptohack.org/ecbcbcwtf/decrypt/" + ciphertext).json()["plaintext"]
plaintext = plaintext[32:]
print(xor_byte(bytes.fromhex(ciphertext), bytes.fromhex(plaintext)))
