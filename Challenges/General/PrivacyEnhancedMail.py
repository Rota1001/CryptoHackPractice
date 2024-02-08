from Crypto.PublicKey import RSA

with open("privacy_enhanced_mail.pem", "rb") as f:
    d = RSA.import_key(f.read())
    print(d.n)