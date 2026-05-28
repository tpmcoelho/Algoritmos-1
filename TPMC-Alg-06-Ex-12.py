def classificado(x):
    if len(x) == 1:
        return "A lista tem um só elemento"
    elif len(x) == 0:
        return "A lista está vazia"
    elif x == sorted(x):
        return True
    elif x == sorted(x, reverse=True):
        return True
    return False

def main():
    y = []
    while True:
        x = input("Digite algo: \n")
        if x == "":
            break
        x = int(x)
        y.append(x)
    print(classificado(y))

main()