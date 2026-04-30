def quociente(x, y):
    resultado = x/y
    return resultado

def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = quociente(a, b)
    print (f"O quociente de {a} e {b} é: {c}")
    return
    
main()