from pwn import *
import json
from Crypto.Util.number import *
import time
r = remote("socket.cryptohack.org", 13398)
r.recvuntil(b"\n")
result = b""
for n in range(0, 100000000000000000, 8):
    ans = 0
    for i in range(n + 7, n - 1, -1):
        x = time.time()
        for j in range(10):
            data = {}
            data["option"] = "get_bit"
            data["i"] = i
            r.sendline(str(data).replace("\'", "\"").encode())
            recv = json.loads(r.recvline().decode())
            if "error" in recv:
                exit(0)
            k = int(recv["bit"], 16)
        y = time.time()
        ans <<= 1
        if (y - x) * 1000 > 3500:
            ans += 1
    result += long_to_bytes(ans)
    print(result)

    


#11000110