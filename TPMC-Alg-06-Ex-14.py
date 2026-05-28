def precedencia(x):
    if x in ["+", "-"]:
        return 1
    elif x in ["*", "/"]:
        return 2
    elif x in ["^"]:
        return 3
    else:
        return -1
    
def main():
    x = input("Digite o operadpor de uma expressão: ")
    print(f"A precedência do operador {x} é: {precedencia(x)}")

main()