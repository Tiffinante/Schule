import random
import time
'''
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
'''
print("Aufgabe 2.3")
hh = int(input("hh:"))
mm = int(input("mm:"))
ss = int(input("ss:"))
add_ss = int(input("add ss:"))
x = ss
y = hh

if add_ss > 60:
    print("Fehler!")

if hh == 24 and mm == 0 and ss == 00:
    print("Der Maximale wert wurde erreicht!")
    print('0:0:1')

elif mm > 59 or ss > 59 or hh > 23:
    print("Fehler!")
else:
    if ss == 59:
        ss = 0

        if mm == 59:
            mm = 0

            if hh == 24:
                hh = 0
                mm = 0
                ss = 1
            else:
                hh += 1

        else:
            if not(hh == 24):
                mm += 1

    else:
        ss += add_ss
        if ss >= 60:
            ss = add_ss - x
            mm += 1
            if mm >= 60:
                mm = 0
                hh += 1

    print(f'{hh}:{mm}:{ss}')
