def hipotenusa (a, b, c):
    min1 = min (a, b)
    min2 = min (a, c)
    print (min1)
    print (min2)
    
def main ():
    a = int(input("Digite o comprimento do primeiro lado do triângulo"))
    b = int(input("Digite o comprimento do segundo lado do triângulo"))
    c = int(input("Digite o comprimento do terceiro lado do triângulo"))
    hipotenusa(a, b, c)
        
main()