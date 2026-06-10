import random
def criarCartela():
    cartela = {}
    letras = ["B", "I", "N", "G", "O"]
    for i in range(len(letras)):
        inicio = i * 15 + 1
        fim = inicio + 15
        cartela[letras[i]] = random.sample(range(inicio, fim), 5)
    return cartela

def verificarVencedora(cartela):
    letras = ["B", "I", "N", "G", "O"]
    for letra in letras:
        if sum(cartela[letra]) == 0:
            return True
    for i in range(5):
        soma_linha = 0
        for letra in letras:
            soma_linha += cartela[letra][i]
        if soma_linha == 0:
            return True
    soma_diag1 = 0
    soma_diag2 = 0
    for i in range(5):
        soma_diag1 += cartela[letras[i]][i]
        soma_diag2 += cartela[letras[i]][4 - i]
    if soma_diag1 == 0 or soma_diag2 == 0:
        return True
    return False

def gerarGlobosDeSorteio():
    letras = ["B", "I", "N", "G", "O"]
    bolas = []
    for i in range(len(letras)):
        letra = letras[i]
        for numero in range(i * 15 + 1, (i + 1) * 15 + 1):
            bolas.append((letra, numero))
    random.shuffle(bolas)
    return bolas

def marcarCartela(cartela, letra, numero):
    if letra in cartela:
        for i in range(5):
            if cartela[letra][i] == numero:
                cartela[letra][i] = 0

def simularPartida():
    cartela = criarCartela()
    bolas = gerarGlobosDeSorteio()
    chamadas = 0
    for letra, numero in bolas:
        chamadas += 1
        marcarCartela(cartela, letra, numero)
        if verificarVencedora(cartela):
            return chamadas, cartela

def main():
    total_chamadas = []
    ultima_cartela = None
    for _ in range(1000):
        chamadas, cartela = simularPartida()
        total_chamadas.append(chamadas)
        ultima_cartela = cartela
    minimo = min(total_chamadas)
    maximo = max(total_chamadas)
    medio = sum(total_chamadas) / len(total_chamadas)
    print(f"Minimo: {minimo}")
    print(f"Medio:  {medio:.2f}")
    print(f"Maximo: {maximo}")
    print("-" * 25)
    letras = ["B", "I", "N", "G", "O"]
    print("| " + "    ".join(letras) + " |")
    print("-" * 25)
    for i in range(5):
        linha_texto = []
        for letra in letras:
            linha_texto.append(f"{ultima_cartela[letra][i]:^3}")
        print("| " + "  ".join(linha_texto) + " |")
    print("-" * 25)

main()