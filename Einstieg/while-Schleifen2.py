import random as r

runden = 0
print("Zahlenraten [51 - 10000] ")
zahl = r.randint(51, 10000)
str_zahl = str(zahl)
# print(zahl)

while True:
    answer = int(input(""))
    if answer > 50:
        runden += 1
        if answer == zahl:
            print("HGW du hast es erraten")
            break
        elif answer > zahl:
            print("Kleiner")
            if runden == 5:
                print(f'Die zahl hat {len(str_zahl)} stellen')
            elif runden == 10:
                print(f'Die erste stelle der zahl ist eine {str_zahl[0]}')
        elif answer < zahl:
            print("Größer")
            if runden == 5:
                print(f'Die zahl hat {len(str_zahl)} stellen')
            elif runden == 10:
                print(f'Die erste stelle der zahl ist eine {str_zahl[0]}')
    else:
        print("Die Zahl ist größer als 50!")

print("Summe")
# Schreibe ein Programm welches die Summe der Zahlen von 1 bis 100 berechnet.
zahl = r.randint(1, 100)
summe = 0
while zahl > 0:
    summe += zahl
    zahl -= 1
print(summe)


print("Kredit")
kredites = int(input("die Höhe des Kredites:"))
zinssatz = int(input("der Zinssatz in Prozent:"))
rueckzahlungsbetrag = int(input("der jährlicher Rückzahlungsbetrag (Tilgung + Zinsen):"))
jahr = int(input("von jahr:"))


while True:
    zinsen = (kredites * zinssatz) // 100
    tillgung = rueckzahlungsbetrag - zinsen
    rest = kredites - tillgung
    if "-" in str(rest):
        break
    txt = "{:^4}-> \t|\t Zinsen: {:^4}€ \t|\t Tillgung: {:^4}€ \t|\t Rest: {:^4}€".format(jahr, zinsen, tillgung, rest)
    print(txt)
    jahr += 1
    kredites = rest
print("Restforderung: \t\t {:^4}€".format(kredites))
