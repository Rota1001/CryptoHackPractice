import random
def add(P: tuple, Q: tuple, B: int, A: int, p: int) -> tuple:
    #By^2 = x^3 + Ax^2 + x
    x1, y1 = P
    x2, y2 = Q
    if P != Q:
        k = (y2 - y1) * pow(x2 - x1, -1, p) 
        x3 = (B * k * k - A - x1 - x2) % p
        y3 = (k * (x1 - x3) - y1) % p
        return (x3, y3)
    k = (3 * x1 * x1 + 2 * A * x1 + 1) * pow(2 * B * y1, -1, p)
    x3 = (B * k * k - A - 2 * x1) % p
    y3 = (k * (x1 - x3) - y1) % p
    return (x3, y3)

def times(x: tuple, n: int, B: int, A: int, p: int) -> tuple:
    if n == 0:
        return (0, 0)
    k = 0
    tmp = n
    while tmp:
        k += 1
        tmp >>= 1
    y = add(x, x, B, A, p)
    for i in range(k - 2, -1, -1):
        if (n >> i) & 1:
            x = add(x, y, B, A, p)
            y = add(y, y, B, A, p)
        else:
            y = add(x, y, B, A, p)
            x = add(x, x, B, A, p)
    return x

def sqrt(a, p):
    b = random.randint(1, p)
    while(pow(b, (p - 1) // 2, p) == 1):
        b = random.randint(1, p)
    t = p - 1
    s = 0
    while t % 2 == 0:
        t >>= 1
        s += 1
    x = pow(a, (t + 1) // 2, p)
    e = pow(a, t, p)
    for k in range(1, s):
        if pow(e, 1 << (s - k - 1), p) != 1:
            x = x * pow(b, (1 << (k - 1)) * t, p) % p
        e = pow(a, -1, p) * x % p * x % p
    return x

p = (1 << 255) - 19
A = 486662
B = 1
n = 0x1337c0decafe
x = 9
y = sqrt((x ** 3 + A * x ** 2 + x) * pow(B, -1, p) % p, p)
G = (x, y)
ans = times(G, n, B, A, p)
print(ans[0])