def tokens (x):
    tokens = []
    i = 0
    while i in len(x):
        c = x[i]
        if c == " ":
            i = i + 1
            continue
        elif c in "+-":
            tokens.append(c)
        elif c.isdigit:
            tokens.append(c)
    return tokens
    
def main():
    x = input("Digite a sua expressão matemática")
    print (f"Os tokens baseados na sua ecpressão matemática são: {tokens(x)}")
    
main ()