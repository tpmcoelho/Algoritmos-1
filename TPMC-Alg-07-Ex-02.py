def diferenca_simetrica(M, N):
    lista = []
    for x in M:
        if x not in N:
            lista.append(x)
    for x in N:
        if x not in M:
            lista.append(x)
    lista.sort()
    return lista

def main():
    M = set()
    N = set()
    x = int(input("Quantos números terá M? "))
    for i in range(x):
        M.add(int(input("Digite um número para M: ")))
    y = int(input("Quantos números terá N? "))
    for i in range(y):
        N.add(int(input("Digite um número para N: ")))
    print(diferenca_simetrica(M, N))

main()