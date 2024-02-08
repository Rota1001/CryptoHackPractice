from Crypto.PublicKey import RSA

with open("rsa-example-cert.der", "rb") as f:
    k = RSA.import_key(f.read())

print(k.n)