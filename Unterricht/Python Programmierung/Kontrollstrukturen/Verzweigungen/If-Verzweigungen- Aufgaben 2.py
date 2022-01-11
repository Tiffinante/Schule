import random

print("Aufgabe 2.1")
dogs_age = int(input("Alter in hundejahren:"))
if dogs_age == 1:
    print(14)
elif dogs_age == 2:
    print(22)
elif dogs_age > 2:
    dogs_age -= 2
    dogs_age *= 5
    dogs_age += 22
    print(dogs_age)

print("Aufgabe 2.2")
x = 0
punkte = 0
while True:
    ergebnis1 = random.randint(0, 13)
    ergebnis2 = random.randint(0, 13)
    # print(ergebnis1, ergebnis2)

    tipp1 = int(input("tipp 1 --> Heim Tore:"))
    tipp2 = int(input("tipp 2 --> Auswärts Tore"))

    # Punkte 3
    if ergebnis1 == tipp1 and ergebnis2 == tipp2:
        print("Ergebnis: ", ergebnis1, ":", ergebnis2, ", Tipp: ", tipp1, ":", tipp2, " -> Punkte 3", sep="")
        punkte += 3
        print("Aktuelle Punkte ->", punkte)
    # Punkte 1
    elif (ergebnis1 > ergebnis2 and tipp1 > tipp2) or (ergebnis1 < ergebnis2 and tipp1 < tipp2) or \
            (ergebnis1 == ergebnis2 and tipp1 == tipp2):
        print("Ergebnis: ", ergebnis1, ":", ergebnis2, ", Tipp: ", tipp1, ":", tipp2, " -> Punkte 1", sep="")
        punkte += 1
        print("Aktuelle Punkte ->", punkte)
    # Punkte 0
    else:
        print("Ergebnis: ", ergebnis1, ":", ergebnis2, ", Tipp: ", tipp1, ":", tipp2, " -> Punkte 0", sep="")
        print("Aktuelle Punkte ->", punkte)
    print(" ")

    x += 1
    if x == 3:
        break

if punkte <= 1:
    print(punkte, "punkte, guter Versuch...")
elif punkte <= 3:
    print(punkte, "punkte, nicht schlecht!")
elif punkte <= 8:
    print(punkte, "punkte, du hast aber Glück.")
elif punkte == 9:
    print(punkte, "punkte, WOW! Kommst du aus der Zukunft?")

print("Aufgabe 2.3")
h = int(input("h:"))
m = int(input("m:"))
s = int(input("s:"))
print("Maxilam zu addirende sekunden sind 60")
add_s = int(input("add s:"))


if s > 59 or m > 59 or h > 23:
    print(f'{h}:{m}:{s} ist ungültig!')
    print("Die maximale uhrzeit ist 23:59:59 !")
    if add_s >= 60:
        print("Die max add s sind 60!")
else:
    if add_s + s > 60:
        s = (add_s + s) - 60
    elif add_s + s == 60:
        s = 0
        m += 1
    else:
        s += add_s
    if m >= 60:
        h += 1
        m = 0
    if h >= 24:
        h = 0
    # Formatirung
    if len(str(h)) == 1:
        h = "0" + str(h)
        print(h)
    if len(str(m)) == 1:
        m = "0" + str(m)
    if len(str(s)) == 1:
        s = "0" + str(s)
    print(f'{h}:{m}:{s}')
