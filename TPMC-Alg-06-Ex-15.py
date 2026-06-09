def tokenizar(expressao):
    tokens = []
    numero = ""
    i = 0

    while i < len(expressao):
        c = expressao[i]

        if c == " ":
            i += 1
            continue

        elif c in "*/()":
            if numero != "":
                tokens.append(numero)
                numero = ""
            tokens.append(c)

        elif c in "+-":
            j = i - 1

            while j >= 0 and expressao[j] == " ":
                j -= 1

            if j >= 0 and (expressao[j].isdigit() or expressao[j] == ')'):
                if numero != "":
                    tokens.append(numero)
                    numero = ""
                tokens.append(c)
            else:
                numero += c

        else:
            numero += c

        i += 1

    if numero != "":
        tokens.append(numero)

    return tokens

def main():
    expressao = input("Digite uma expressão matemática: ")
    print(tokenizar(expressao))

main()