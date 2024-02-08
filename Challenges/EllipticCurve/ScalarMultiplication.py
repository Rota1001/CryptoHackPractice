def add(p: tuple, q: tuple, a: int, mod: int) -> tuple:
    x1, y1 = p
    x2, y2 = q
    zero = (0, 0)
    k: int
    if p == zero:
        return q
    if q == zero:
        return p
    if x1 == x2 and y1 == -y2:
        return zero
    if p != q:
        k = (y2 - y1) * pow(x2 - x1, -1, mod)
    else:
        k = (3 * x1 * x1 + a) * pow(2 * y1, -1, mod)
    x3 = k * k - x1 - x2
    y3 = k * (x1 - x3) - y1
    x3 %= mod
    y3 %= mod
    return (x3, y3)

def times(x: tuple, n: int, a: int, mod: int) -> tuple:
    ret = (0, 0)
    while n:
        if n & 1:
            ret = add(ret, x, a, mod)
        x = add(x, x, a, mod)
        n >>= 1
    return ret

P = (2339, 2213)
mod = 9739
a = 497

print(times(P, 7863, a, mod))