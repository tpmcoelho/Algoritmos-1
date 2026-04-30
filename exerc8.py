def num_int_pos():
    x = int(input("Digite um número inteiro positivo maior que zero\n"))
    if x <= 0:
        print ("Valor inválido")
    y = x
    x = str(x)
    x = len(x)
    print (f"O número {y} tem {x} dígitos")
num_int_pos()