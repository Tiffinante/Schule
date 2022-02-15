invoice = [
    # Tupel: Anzahl, Artikelnummer, Beschreibung, Einzelpreis
    (2, "57620676", "Tastatur", 24.95),
    (3, "29878362", "Kabelbinder 6mm, 50 St.", 3.43),
    (1, "47923243", "WLAN Access Point", 123.21)
]

print("{:<5}{:<10}{:<15}{:<28}{:>20}{:>20}".format("Pos.", "Anzahl", "Art.-Nr.", "Beschreibung", "Einzelpreis",
                                                   "Gesamtpreis"))
for i in range(len(invoice)):
    a = invoice[i][0]
    b = invoice[i][1]
    c = invoice[i][2]
    d = invoice[i][3]
    print("{:<5}{:<10}{:<15}{:<28}{:>20}{:>20}".format(i+1, a, b, c, d, d*a))
