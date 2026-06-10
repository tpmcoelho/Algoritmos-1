def buscaReversa(a, b):
    r = []
    for chave, valor in a.items():
        if valor == b:
            r.append(chave)
    return r

def main():
    x = {
        "Caneta": 2.50,
        "Lápis": 1.50,
        "Borracha": 1.50,
        "Caderno": 15.00,
        "Apontador": 1.50,
        "Régua": 3.00
    }

    w = float(input("Digite o preço que deseja buscar: "))
    result = buscaReversa(x, w)
    print(f"Chaves com o valor {w}: {result}")

main()