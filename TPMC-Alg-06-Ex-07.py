def divisores(a):
    x=[]
    for i in range (1, a):
        if a % i == 0:
            x.append(i)
    return x

def numero_perfeito(a, b):
    if sum(b) == a:
        return True
    else:
        return False

def main():
    x = int(input("Digite um número para saber seus divisores:\n"))
    print (f"Os divisores de {x} são: {divisores(x)}")
    y = divisores(x)
    print (numero_perfeito(x, y))
        
main()