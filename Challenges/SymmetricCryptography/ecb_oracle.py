import requests
import string

def send_request(plaintext):
    req = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/" + plaintext.hex())
    return req.json()["ciphertext"]

flag = b"crypto{"

alphabet = '_' + '@' + '}' + string.digits + string.ascii_lowercase + string.ascii_uppercase

for i in range(7, 30):
    text = b"\x00" * (31 - i)
    result = send_request(text)[32:64]
    for j in alphabet:
        query = text + flag + j.encode()
        print(query)
        res = send_request(query)[32:64]
        # print(res)
       # print(result)
        if res == result:
            flag += j.encode()
            break
    print(flag)

