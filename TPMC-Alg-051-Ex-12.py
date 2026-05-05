def encaixa (x, y):
    x1 = len (str(x))
    x2 = len (str(y))
    x3 = min (x1, x2)
    x4 = str (x)
    x5 = str (y)
    z = 0
    for i in range (1, (x3 + 1)):
        if x4 [-i] == x5 [-i]:
            z = z + 1
            if z == x3:
                w = True
        else:
            w = False
            
    return w                
        
def main():
    a = int(input("Digite um número inteiro:"))
    b = int(input("Digite outro número inteiro"))
    if encaixa(a, b) == True:
        print (f"{b} encaixa em {a}")
    elif encaixa(a, b) == False:
        print (f"{b} Não encaixa em {a}")
        
main()