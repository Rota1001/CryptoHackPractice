from pwn import *
import json
# from ecdsa.ecdsa import generator_192
# print(generator_192.x())
# print(generator_192.y())
# print(generator_192.curve())

r = remote("socket.cryptohack.org", 13381)
data = {}
data["option"] = "sign_time"
print(str(data))
r.sendlineafter(b"\n", str(data).replace('\'', '\"').encode())
data = json.loads(r.recvline().decode())
print(data)
# data["option"] = "verify"
# print(data)
# r.sendline(str(data).replace('\'', '\"').encode())
# print(r.recvline())