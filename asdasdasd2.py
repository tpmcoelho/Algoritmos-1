nome = ""
n = 0
def imprime_n_vezes(nome, n):
    nome = input("Digite algo: ")
    n = int(input("Digite um número: "))
    for i in range(n):
        print(f"{nome}")
imprime_n_vezes(nome, n)