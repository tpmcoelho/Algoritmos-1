def divisores(a):
    x=[]
    for i in range (1, a):
        if a % i == 0:
            x.append(i)
    return x

def numero_perfeito(a, b):
    if sum(b) == a:
        return True
    else:
        return False

def main():
    for x in range(1, 10001):
        y = divisores(x)
        if numero_perfeito(x, y):
            print(f"{x} é perfeito.")

main()