

# This file was *autogenerated* from the file /home/rota1001/ctf/CryptoHackPractice/Challenges/EllipticCurve/test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_13381 = Integer(13381); _sage_const_100 = Integer(100); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_16 = Integer(16)
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
rr = remote("socket.cryptohack.org", int(_sage_const_13381 ))
rr.recvline()
for i in range(_sage_const_100 ):
    data = {}
    data["option"] = "sign_time"
    rr.sendline(str(data).replace("\'", "\"").encode())
    k = json.loads(rr.recvline().decode().strip())
    sec = k['msg'].strip().split(':')[-_sage_const_1 ]
    print(sec)
    if sec == "2":
        print("success")
        msg = k['msg']
        s = k['s']
        r = k['r']
        break
    if sec == "59":
        sleep(_sage_const_2 )
    elif sec == "58":
        sleep(_sage_const_3 )

print(msg)
print(s)
print(r)
s = int(s, _sage_const_16 )
r = int(r, _sage_const_16 )
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

