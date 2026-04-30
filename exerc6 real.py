import random
def sorteia_dado():
    x = random.randint(1, 6)
    return x

def main():
    print(sorteia_dado())
    
main()