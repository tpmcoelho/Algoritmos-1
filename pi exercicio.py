a = 3
b = 2 
c = 3
d = 4 
pi = 0
print (a)
for i in range (14):
    if i == 0:
        pi = pi + a
    if i % 2 == 0:
        pi1 = 4/(b*c*d)
        pi = pi + pi1
    elif i % 2 != 0:
        pi2 = (4/(b*c*d)) * (-1)
        pi = pi + pi2
    b = b + 2
    c = c + 2 
    d = d + 2   
    print (pi)