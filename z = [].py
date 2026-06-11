c = []
def diferenca_conjuntos(m, n):
    for x in m:
        if x not in n:
            c.append(x)
    for x in n:
        if x not in m:
            c.append(x)
    c.sort()
    return c

def main():
    z = set()
    w = set()
    while True:
        x = input()
        if x == "":
            break
        x = int(x)
        z.add(x)
    while True:
        y = input()
        if y == "":
            break
        y = int(y)
        w.add(y)
    print (diferenca_conjuntos(z, w))

main()