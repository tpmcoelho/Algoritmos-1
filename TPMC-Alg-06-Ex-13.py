def countRange(a, b, c):
    count = 0
    for i in c:
        if a <= i < b:
            count += 1
    return count

def main():
    x = int(input("Digite um valor mínimo: "))
    y = int(input("Digite um valor máximo: "))
    r = []
    while True:
        z = input("Digite um valor (enter para sair): ")
        if z == "":
            break
        z = int(z)
        r.append(z)
    count = countRange(x, y, r)
    print(f"A quantidade de valores no intervalo [{x}, {y}] é {count}")

main()