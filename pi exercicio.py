a = 3
i = 1
pi = 0
for i in range (15):
    if i % 2 == 0:
        pi1 = a + 4/(2*i*3*i*4*1)
        pi = pi + pi1
    elif i % 2 != 0:
        pi1 = (a + 4/(2*i*3*i*4*1)) * (-1)
        pi = pi + pi1
print (pi)
