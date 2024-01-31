import requests



ciphertext = bytes.fromhex(requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/").json()["ciphertext"])
iv, ciphertext = ciphertext[:16], ciphertext[16:]

flag = bytes.fromhex(requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{ciphertext.hex()}/{iv.hex()}").json()["ciphertext"])
print(flag)