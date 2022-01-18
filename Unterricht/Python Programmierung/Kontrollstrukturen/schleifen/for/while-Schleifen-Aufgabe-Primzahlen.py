# Primzahltest
n = int(input("Teste ob es eine Pimzahl ist:"))
if n <= 0:
    print("Bitte keine 0")
else:
    for i in range(2, round(n / 2) + 1):
        if (n % i) == 0:
            print("ist keine")
            break
    else:
        print("es ist eine")


# Primzahlfunktion
while True:
    stop = False
    n = int(input("Eine Primzahl bitte:"))
    if n <= 0:
        print("Bitte keine 0")
    else:
        for i in range(2, round(n / 2) + 1):
            if (n % i) == 0:
                print("ist keine Primzahl")
                break
            else:
                for i in range(n, n * 2):
                    is_pz = True
                    for t in range(2, int(i / 2) + 1):
                        if i % t == 0 and t < i:
                            is_pz = False
                            break
                    if is_pz:
                        if not(i == n):
                            print("Die nächste Primzahl wäre ", i)
                            stop = True
                            break
                        if stop:
                            break
    if stop:
        break

# Primzahlgenerator
max = int(input("Primzahlen bis:"))
for i in range(1, max + 1):
    is_pz = True
    for t in range(2, int(i / 2) + 1):
        if i % t == 0 and t < i:
            is_pz = False
            break
    if is_pz:
        print(i, end=" ")

# Primfaktorenzerlegung
n = int(input("\nWelche Zahl möchtest du Zerlegen: "))
i, counter = 2, 0
while i <= n:
    while n % i == 0:
        if not(counter == 0):
            print("* ", end="")
        print (i, end=" ")
        n /= i
        counter += 1
    i += 1
if counter < 2:
    print("* 1", end="")
