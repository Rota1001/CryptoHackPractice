

def check(g, p):
    for i in range(2, p):
        if pow(g, i, p) == g:
            return False
    return True


g = 2
p = 28151

while not check(g, p):
    g += 1

print(g)