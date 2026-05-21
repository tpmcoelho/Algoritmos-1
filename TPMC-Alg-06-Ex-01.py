y = []
while True:
    x = int(input("Digite números para entrar na sua lista (0 para sair):\n"))
    if x == 0:
        break
    y.append(x)
    
y.sort()
print (f"Sua lista em ordem crescente é {y}")