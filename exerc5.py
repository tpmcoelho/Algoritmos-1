x = 0 
y = 0
b = 0
def potencia(x, y, b):
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    b=x
    for i in range(y - 1):
        x = b * x
    print(x)
potencia(x, y, b)