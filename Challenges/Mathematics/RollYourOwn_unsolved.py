#unsolved
from pwn import *
from gmpy2 import gmpy2

r = remote("socket.cryptohack.org", 13403)

recv = r.recvline().decode().split(' ')[-1].strip()[1:-1]
q = int(recv, 16)

k = 2
while not gmpy2.is_prime(k * q + 1):
    k += 1

p = k * q + 1
g = pow(2, k, p)
data = {}
data["g"] = hex(g)
data["n"] = hex(p)

r.sendlineafter(b": ", str(data).replace("\'", "\""))
print(r.recvline())
