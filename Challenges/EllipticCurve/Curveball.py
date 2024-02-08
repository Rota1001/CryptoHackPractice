from pwn import *


r = remote("socket.cryptohack.org", 13382)

data = {}
data["private_key"] = 115792089210356248762697446949407573529996955224135760342422259061068512044370
data["host"] = 'www.bing.com'
data["generator"] = [0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A]
data["curve"] = "dsa"

r.sendlineafter(b"\n", str(data).replace("\'", "\"").encode())
print(r.recvline())
