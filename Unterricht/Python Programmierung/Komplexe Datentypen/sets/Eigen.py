print("set comprehension")

print("\n1x1")
aeusere_liste = [a * b for a in range(1, 11) for b in range(1, 11)]
print(aeusere_liste)

print("\nnumbers aus 1x1")
numbers_1x1 = {a * b for a in range(1, 11) for b in range(1, 11)}
print(numbers_1x1)
