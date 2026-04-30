def imprime_n_vezes(nome, n):
    for i in range (n):
        print (nome)

def main():
    x = input("Escreva algo\n")
    y = int(input("Digite um número\n"))
    imprime_n_vezes(x, y)
    
main()