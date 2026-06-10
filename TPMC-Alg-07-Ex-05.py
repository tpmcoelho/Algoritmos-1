def mapearLetras(palavra):
    contagem = {}
    for letra in palavra.lower():
        if letra != " ":
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1    
    return contagem

def Anagrama(a, b):
    return mapearLetras(a) == mapearLetras(b)

def main():
    x = input("Digite a primeira palavra: ")
    y = input("Digite a segunda palavra: ")
    resultado = Anagrama(x, y)
    print(resultado)

main()