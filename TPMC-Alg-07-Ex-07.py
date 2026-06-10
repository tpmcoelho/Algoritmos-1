import random
def criarCartela():
    cartela = {}
    letras = ["B", "I", "N", "G", "O"]
    for i in range(len(letras)):
        inicio = i * 15 + 1
        fim = inicio + 15
        cartela[letras[i]] = random.sample(range(inicio, fim), 5)
    return cartela

def exibirCartela(cartela):
    letras = ["B", "I", "N", "G", "O"]
    for letra in letras:
        print(f"{letra:^5}", end="")
    print()
    print("-" * 25)
    for i in range(5):
        for letra in letras:
            print(f"{cartela[letra][i]:^5}", end="")
        print()

def main():
    x = criarCartela()
    exibirCartela(x)

main()