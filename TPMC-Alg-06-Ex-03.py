def remov_extr(n):
    n.pop(len(n) - 2)
    n.pop(len(n) - 1)
    n.pop(1)
    n.pop(0)
    return n
        
def main():
    y = []
    while True:
        x = int(input("Digite números para entrar na sua lista (0 para sair):\n"))
        if x == 0:
            break
        y.append(x)
    if len(y) <= 4:
        print ("Erro, favor inserir mais de 4 valores.")   
        main()
    y.sort()
    print (f"Lista antiga: {y}")
    print (f"Lista nova:   {remov_extr(y)}")

main()