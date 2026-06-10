def Vencedora(cartela):
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
    print("-" * 25)

def main():
    coluna = {
        "B": [0, 0, 0, 0, 0],
        "I": [16, 17, 18, 19, 20],
        "N": [31, 32, 33, 34, 35],
        "G": [46, 47, 48, 49, 50],
        "O": [61, 62, 63, 64, 65]
    }
    linha = {
        "B": [1, 2, 0, 4, 5],
        "I": [16, 17, 0, 19, 20],
        "N": [31, 32, 0, 34, 35],
        "G": [46, 47, 0, 49, 50],
        "O": [61, 62, 0, 64, 65]
    }
    diagonal = {
        "B": [0, 2, 3, 4, 5],
        "I": [16, 0, 18, 19, 20],
        "N": [31, 32, 0, 34, 35],
        "G": [46, 47, 48, 0, 50],
        "O": [61, 62, 63, 64, 0]
    }
    perdedora = {
        "B": [0, 2, 3, 0, 5],
        "I": [16, 0, 18, 19, 20],
        "N": [31, 32, 33, 34, 35],
        "G": [46, 47, 48, 0, 50],
        "O": [61, 62, 0, 64, 65]
    }
    
    print("1. Testando Cartela com COLUNA Vencedora (B):")
    exibirCartela(coluna)
    print("Vencedora?", Vencedora(coluna))
    print("\n" + "="*40 + "\n")
    print("2. Testando Cartela com LINHA Vencedora (Linha do meio):")
    exibirCartela(linha)
    print("Vencedora?", Vencedora(linha))
    print("\n" + "="*40 + "\n")
    print("3. Testando Cartela com DIAGONAL Vencedora:")
    exibirCartela(diagonal)
    print("Vencedora?", Vencedora(diagonal))
    print("\n" + "="*40 + "\n") 
    print("4. Testando Cartela com ALGUNS ZEROS (Não Vencedora):")
    exibirCartela(perdedora)
    print("Vencedora?", Vencedora(perdedora))

main()