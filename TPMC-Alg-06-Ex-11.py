import random
y =[]
for i in range(6):
    x = random.randint(1, 60)
    y.append(x)
y.sort()
print(f"Os números da mega da virada são: {y}")