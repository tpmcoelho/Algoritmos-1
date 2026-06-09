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

def precedencia(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2

def infix_para_postfix(w):
    posfix = []
    op = []
    for token in w:
        if token.lstrip("+-").isdigit():
            posfix.append(token)

        elif token in "+-*/":
            while (len(op) > 0 and
                   op[-1] != "(" and
                   precedencia(token) <= precedencia(op[-1])):
                posfix.append(op.pop())
            op.append(token)
        elif token == "(":
            op.append(token)
        elif token == ")":
            while op[-1] != "(":
                posfix.append(op.pop())
            op.pop()
    while len(op) > 0:
        posfix.append(op.pop())
    return posfix

def main():
    expressao = input("Digite a expressão: ")
    tokens = tokenizar(expressao)
    posfix = infix_para_postfix(tokens)
    print(f"A expressão na forma pós fixada fica: {posfix}")

main()