def encaixa (x, y):
    m = min (x, y)
    z = str (x)
    w = str (y)
    if m == x:
        if z in w:
            return "caso1"
        elif z not in w: 
            return "caso3"
    elif m == y:
        if w in z:
            return "caso2"
        elif w not in z:
            return "caso4"
            
def main():
    a = int(input("Digite um número inteiro:\n"))
    b = int(input("Digite outro número inteiro:\n"))
    if encaixa(a, b) == "caso1":
        print (f"{a} é segmento de {b}")
    elif encaixa(a, b) == "caso3":
        print (f"{a} não é segmento de {b}")
    elif encaixa(a, b) == "caso2":
        print (f"{b} é segmento de {a}")
    elif encaixa(a, b) == "caso4":
        print (f"{b} não é segmento de {a}")
        
main()