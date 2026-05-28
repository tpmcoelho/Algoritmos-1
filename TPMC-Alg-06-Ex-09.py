notas = []
while True:
    x = input("Digite a nota do aluno (enter para sair):")
    if x == "":
        break
    x = float(x)
    notas.append(x)
a = []
b = []
c = []
media = sum(notas) / len(notas)
for i in notas:
    if i < media:
        a.append(i)
    elif i == media:
        b.append(i)
    else:
        c.append(i)
print(f"Media: {media:.2f}")
print(a)
print(b)
print(c)