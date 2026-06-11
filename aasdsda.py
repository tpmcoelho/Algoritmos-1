def unico (x,y):
    c = len(x) == len(y)
    return c

def main():
    x = input()
    y = set(x)
    print (unico (x, y)) 

main()