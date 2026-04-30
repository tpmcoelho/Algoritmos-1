import random
def sorteia_dado ():
    a = 0
    b = 0
    c = 0
    d = 0  
    e = 0
    f = 0
    for i in range (1000000):
        x = random.randint(1, 6)
        if x == 1:
            a = a + 1
        if x == 2:
            b = b + 1
        if x == 3:
            c = c + 1
        if x == 4:
            d = d + 1
        if x == 5:
            e = e + 1
        if x == 6:
            f = f + 1
    print (f"A quantidade de números 1 é: {a}")
    print (f"A quantidade de números 2 é: {b}")
    print (f"A quantidade de números 3 é: {c}")
    print (f"A quantidade de números 4 é: {d}")
    print (f"A quantidade de números 5 é: {e}")
    print (f"A quantidade de números 6 é: {f}")
sorteia_dado()