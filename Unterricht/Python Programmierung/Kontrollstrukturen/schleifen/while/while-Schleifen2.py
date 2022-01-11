import random as r

runden = 0
print("Zahlenraten [51 - 10000] ")
zahl = r.randint(51, 10000)
str_zahl = str(zahl)
print(zahl)

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
    zinsen = (kredites * zinssatz) / 100
    tillgung = rueckzahlungsbetrag - zinsen
    rest = kredites - tillgung
    if "-" in str(rest):
        break
    txt = f"{jahr:>8.2f} -> \t|\t Zinsen: {zinsen:>8.2f}€ \t|\t Tillgung: {tillgung:>8.2f}€ \t|\t Rest: {rest:>8.2f}€"
    print(txt)
    jahr += 1
    kredites = rest
print(f"Restforderung: \t\t\t\t {kredites:>8.2f}€")

# Andere Möglichkeit
'''while True:
    zinsen = (kredites * zinssatz) / 100
    tillgung = rueckzahlungsbetrag - zinsen
    rest = kredites - tillgung
    if "-" in str(rest):
        break
    txt = "{:>8.2f}-> \t|\t Zinsen: {:>8.2f}€ \t|\t Tillgung: {:>8.2f}€ \t|\t Rest: {:>8.2f}€".format(int(jahr), int(zinsen), int(tillgung), int(rest))
    print(txt)
    jahr += 1
    kredites = rest
print("Restforderung: \t\t\t {:>8.2f}€".format(kredites))'''

