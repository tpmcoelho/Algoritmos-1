def divisores(a):
    x=[]
    for i in range (1, a+1):
        if a % i == 0:
            x.append(i)
    return x

def main():
    x = int(input("Digite um número para saber seus divisores:\n"))
    print (f"Os divisores de {x} são: {divisores(x)}")
    
main()