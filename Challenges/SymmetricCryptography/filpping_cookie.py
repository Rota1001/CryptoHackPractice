
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

cipher = bytes.fromhex("8e0317086d2f505288036caa501fbd91dedaac5a56959e91539f2fb4d8962f4f9eeb0f431f41dc1a14c67f4fd34b99b4")

before = b"admin=False;expi"
after = b"admin=True; expi"
# print( len(xor(cipher[:16], xor(before, after))))
cipher = xor(cipher[:16], xor(before, after)) + cipher[16:]

print(cipher[:16].hex())
print(cipher[16:].hex())