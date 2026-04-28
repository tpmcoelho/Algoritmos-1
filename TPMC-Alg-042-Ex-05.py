soma = 0

while True:
    x = input("Digite a idade de cada visitante (enter para sair): ")
    if x == "":
        break
    x = int(x)
    if x > 0 and x <= 2:
        soma = soma + 0
    if x >= 3 and x <= 12:
        soma = soma + 14
    if x >= 13 and x <= 64:
        soma = soma + 23
    if x >= 65:
        soma = soma + 18
print (f"O valor total a ser pago é: R${soma:.2f}")