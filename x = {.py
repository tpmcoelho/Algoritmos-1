x = {
    "Daniel": 1,
    "Kaua": 2,
    "Thiago": 3
}
print (x["Daniel"])
print (x.items())
print (x.keys())
print (x.values())
print (list(x.items()))
print (list(x.keys()))
print (list(x.values()))
for i in x:
    print (i)
print (x.get("Daniel"))
print (x.get("Kaua"))
print (x.get("Thiago"))
print (x.get("Abobora"))
print (x.get("Abobora", "N/A"))
for nome, numero in x.itens():
    print (nome, numero, sep="")