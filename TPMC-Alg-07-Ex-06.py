def mapearLetras(frase):
    contagem = {}
    for caractere in frase.lower():
        if caractere.isalpha():
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1   
    return contagem

def Anagrama(frase1, frase2):
    return mapearLetras(frase1) == mapearLetras(frase2)

def main():
    x = input("Digite a primeira frase: ")
    y = input("Digite a segunda frase: ")
    resultado = Anagrama(x, y)
    print(resultado)

main()