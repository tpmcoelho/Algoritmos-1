import random

def sorteia_dado():
    x = random.randint(1, 6)
    return x

def main():
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    for i in range (1000000):
        x = sorteia_dado()
        if x == 1:
            x1 = x1 + 1
        if x == 2:
            x2 = x2 + 1
        if x == 3:
            x3 = x3 + 1
        if x == 4:
            x4 = x4 + 1
        if x == 5:
            x5 = x5 + 1
        if x == 6:
            x6 = x6 + 1
    print(f"O número 1 foi sorteado {x1} vezes\nO número 2 foi sorteado {x2} vezes\nO número 3 foi sorteado {x3} vezes\nO número 4 foi sorteado {x4} vezes\nO número 5 foi sorteado {x5} vezes\nO número 6 foi sorteado {x6} vezes")


main()