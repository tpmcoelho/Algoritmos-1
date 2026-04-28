while True:
    x = input("Digite uma sequência de 8 bits (enter para sair): ")
    if x == "":
        break
    elif (x.count('0') + x.count('1')) != 8 or len(x)!=8 :
        print ("Erro")
        continue
    nums1 = x.count("1")
    if nums1 % 2 != 0:
        print ("1")
    elif nums1 % 2 == 0:
        print ("0")