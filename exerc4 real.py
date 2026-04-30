def quadrado(x):
    resultado = x * x
    return (resultado)

def main():
    a = int(input("Digite um número para saber o seu quadrado\n"))
    print (f"O quadrado de {a} é {quadrado(a)}")
    
main()