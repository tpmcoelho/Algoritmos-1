def formatador(lista):
    if len(lista) == 1:
        return lista[0]
    return ", ".join(lista[:-1]) + " e " + lista[-1]

def main():
    y = []
    while True:
        x = input("Digite algo: ")
        if x == "":
            break
        y.append(x)
    print(formatador(y))

main()