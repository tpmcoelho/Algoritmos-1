def tokenizar(x):
    tokens = []
    y = ""
    i = 0

    while i < len(x):
        c = x[i]

        if c == " ":
            i += 1
            continue

        elif c in "*/()":
            if y != "":
                tokens.append(y)
                y = ""
            tokens.append(c)

        elif c in "+-":
            j = i - 1

            while j >= 0 and x[j] == " ":
                j -= 1

            if j >= 0 and (x[j].isdigit() or x[j] == ')'):
                if y != "":
                    tokens.append(y)
                    y = ""
                tokens.append(c)
            else:
                y += c

        else:
            y += c

        i += 1

    if y != "":
        tokens.append(y)

    return tokens

def main():
    a = input("Digite uma expressão matemática: ")
    print(tokenizar(a))

main()