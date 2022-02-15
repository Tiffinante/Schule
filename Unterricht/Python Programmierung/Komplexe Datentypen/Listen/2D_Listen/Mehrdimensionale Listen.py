print("1x1")

aeusere_liste = [[a * b for a in range(1, 11)] for b in range(1, 11)]
print(aeusere_liste)

print(aeusere_liste[int(input("Zahl 1:")) - 1][int(input("Zahl 2:")) - 1])
