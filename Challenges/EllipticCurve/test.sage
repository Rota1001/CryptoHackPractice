from pwn import *
import json
from ecdsa.ecdsa import generator_192
from sage.all import *
from Crypto.Util.number import *
from hashlib import sha1

g = generator_192
p = g.curve().p()
msg: str
s: int
r: int
rr = remote("socket.cryptohack.org", int(13381))
rr.recvline()
for i in range(100):
    data = {}
    data["option"] = "sign_time"
    rr.sendline(str(data).replace("\'", "\"").encode())
    k = json.loads(rr.recvline().decode().strip())
    sec = k['msg'].strip().split(':')[-1]
    print(sec)
    if sec == "2":
        print("success")
        msg = k['msg']
        s = k['s']
        r = k['r']
        break
    if sec == "59":
        sleep(2)
    elif sec == "58":
        sleep(3)

print(msg)
print(s)
print(r)
s = int(s, 16)
r = int(r, 16)
answer = "unlock"
news = (s + (bytes_to_long(sha1(answer.encode()).digest())) - bytes_to_long(sha1(msg.encode()).digest())) % p
data = {}
data["option"] = "verify"
data["r"] = hex(r)
data["s"] = hex(news)
data["msg"] = answer
rr.sendline(str(data).replace("\'", "\"").encode())
print(rr.recvline())
# k = json.loads(rr.recvline().decode().strip())