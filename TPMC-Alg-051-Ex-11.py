def conta_digitos(n, d):
    n = str(n)
    d = str(d)
    x = n.count(d)
    return x

def main():
    a = int(input("Digite um número inteiro"))
    b = int(input("Digite outro número inteiro"))
    x = 0
    for i in range (1, 10):
        w = conta_digitos (a, i)
        t = conta_digitos (b, i)
        if w == t:
            x = x + 1
            if x == 9:
                c = 1
        else: 
            c = 0
    if c ==1:
        print ("É permutação")
    else:
        print ("Não é permutação")
            
main()