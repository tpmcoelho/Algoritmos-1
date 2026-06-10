def caracteres_unicos(x):
    y = set(x)
    return len(x) == len(y)

def main():
    a = input("Digite uma string: ")
    print(caracteres_unicos(a))

main()