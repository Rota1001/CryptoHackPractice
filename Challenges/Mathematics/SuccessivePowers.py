from gmpy2 import gmpy2


x = 97
num = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
p: int
while True:
    x = gmpy2.next_prime(x)
    if x > 1000:
        break
    b = True
    for i in range(0, len(num) - 2):
        if num[i] * num[i + 2] % x != num[i + 1] ** 2 % x:
            b = False
            break
    if b == True:
        p = x

print(num[1] * pow(num[0], -1, p) % p)
