from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from factordb import factordb
from Crypto.Cipher import PKCS1_OAEP

primes = []




c = bytes.fromhex('249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28')
with open("fast_prime_key.pem", "rb") as f:
    key = RSA.import_key(f.read())

n = key.n
e = key.e

tmp = factordb.FactorDB(n)
tmp.connect()
p, q = tmp.get_factor_list()

phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
m = cipher.decrypt(c)
print(m)


