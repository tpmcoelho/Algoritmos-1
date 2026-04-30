def conta_digitos(n, d):
    n = str(n)
    x = 0
    for i in n:
        if i == str(d):
            x = x + 1
    return x

def main():
    n = int(input("Digite um número inteiro: "))
    d = int(input("Digite um dígito (0-9): "))
    if d < 0 or d > 9:
        print("Dígito inválido. Por favor, digite um dígito entre 0 e 9.")
        return
    x = conta_digitos(n, d)
    print(f"O dígito {d} aparece {x} vezes em {n}.")

main()