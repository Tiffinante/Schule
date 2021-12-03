print("Kredit")
kredites = int(input("die Höhe des Kredites:"))
zinssatz = float(input("der Zinssatz in Prozent:"))
rueckzahlungsbetrag = int(input("der jährlicher Rückzahlungsbetrag (Tilgung + Zinsen):"))
jahr = int(input("von jahr:"))

txt = "{:^5}-> \t|\t Zinsen: {:^5}€ \t|\t Tillgung: {:^5}€ \t|\t Rest: {:^5}€".format(0, 0, 0, 0)

while True:
    zinsen = (kredites * zinssatz) // 100
    tillgung = rueckzahlungsbetrag - zinsen
    rest = kredites - tillgung
    if "-" in str(rest):
        break
    txt = "{:^5}-> \t|\t Zinsen: {:^5}€ \t|\t Tillgung: {:^5}€ \t|\t Rest: {:^5}€".format(jahr, zinsen, tillgung, rest)
    print(txt)
    jahr += 1
    kredites = rest
print(("=" * len(txt)) + "==================")
print("Restforderung: {:^5}€".format(kredites))
