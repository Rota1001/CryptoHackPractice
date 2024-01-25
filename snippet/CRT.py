
def CRT(a, n):
    mul = 1
    for i in n:
        mul *= i
    ret = 0
    for i in range(len(a)):
        ret += (mul // n[i]) * pow(mul // n[i], -1, n[i]) * a[i]
    ret %= mul
    return ret


a = [2, 3, 5]
n = [5, 11, 17]
print(CRT(a, n))