y = []
x = ""
while True:
    x = input("Digite algo (enter para sair):\n")
    if x == "":
        break
    if x not in y:
        y.append(x)
        
for valor in y:
    print (valor)