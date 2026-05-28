import string
x = input("Escreva algo")
x = x.split()
y = []
for item in x:
    resultado = item.translate(str.maketrans('', '', string.punctuation))
    y.append(resultado)
print(y)