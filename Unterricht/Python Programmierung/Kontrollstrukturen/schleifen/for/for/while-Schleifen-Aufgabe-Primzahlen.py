# Primzahltest
k = int(input("Teste ob es eine Pimzahl ist:"))
if k <= 0:
    print("Bitte keine 0")
else:
    for i in range(2, round(k / 2) + 1):
        if (k % i) == 0:
            print("ist keine")
            break
    else:
        print("es ist eine")


# Primzahlgenerator
max = int(input("Primzahlen bis:"))
for i in range(1, max):
    is_pz = True
    for teiler in range(2, int(i / 2) + 1):
        if i % teiler == 0 and teiler < i:
            is_pz = False
            break
    if is_pz:
        print(i, end=" ")
