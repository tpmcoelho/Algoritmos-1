#Recursividade potenciação:
def potenci_rec(x,n):
    if n == 0:
        return 1 
    return x * potenci_rec(x, n-1)

def main():
    x = int(input())
    n = int(input())
    print (potenci_rec(x, n))
    
main()

#Recursividade fatorial:

def fatorial_rec(x):
    if x == 1:
        return 1
    return x * fatorial_rec(x-1)

def main():
    x = int(input())
    print (fatorial_rec(x))
    
main()

def palindromo_rec(x):
    if len(x) == 1 or len(x) == 0:
        return True
    if x[0] == x[-1] and palindromo_rec(x[1:-1]):
        return True
    else: 
        return False

#OU
#def palindromo_rec2(x):
#    return (len(x)==1 or len(x) == 0) or (x[0] == x [-1] and palindromo_rec2(x[1:-1]))

def main():
    x = input()
    print (palindromo_rec(x))
    
main()
    
#Iteratividade:
#for e while