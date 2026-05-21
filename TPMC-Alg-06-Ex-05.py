y = []
while True:
    x = input("Digite números para entrar na sua lista (enter para sair):")
    if x == "":
        break
    x = int(x)
    y.append(x)    
n = []
z = []
p = []
for i in y:
    if i < 0:
        n.append(i)
    elif i == 0:
        z.append(i)
    else:
        p.append(i)    
result = n + z + p
print ("Números organizados:")
for elemento in result:
    print (elemento)