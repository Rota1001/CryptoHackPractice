import random
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

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

print(sqrt(a, p) % p)
        