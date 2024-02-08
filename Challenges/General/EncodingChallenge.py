from pwn import *
from Crypto.Util.number import *
import json
import base64
import codecs

r = remote("socket.cryptohack.org", 13377)

for _ in range(100):
    data = {}
    recv = json.loads(r.recvline().decode().strip())
    if recv['type'] == 'base64':
        data['decoded'] = base64.b64decode(recv['encoded'].encode()).decode()
    elif recv['type'] == 'hex':
        data['decoded'] = bytes.fromhex(recv['encoded']).decode()
    elif recv['type'] == 'rot13':
        data['decoded'] = codecs.decode(recv['encoded'], 'rot_13')
    elif recv['type'] == 'bigint':
        data['decoded'] = bytes.fromhex(recv['encoded'][2:]).decode()
    else:
        tmp = ""
        for i in recv['encoded']:
            tmp += chr(i)
        data['decoded'] = tmp
    r.sendline(str(data).replace("\'", "\""))
    print(_)

print(r.recvline())
    