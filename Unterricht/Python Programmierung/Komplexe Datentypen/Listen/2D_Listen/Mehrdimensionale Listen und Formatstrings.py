invoice = [
    # Tupel: Anzahl, Artikelnummer, Beschreibung, Einzelpreis
    (2, "57620676", "Tastatur", 24.95),
    (3, "29878362", "Kabelbinder 6mm, 50 St.", 3.43),
    (1, "47923243", "WLAN Access Point", 123.21)
]

print("{:<5}{:<10}{:<15}{:<28}{:<10}{:>10}".format("Pos.", "Anzahl", "Art.-Nr.", "Beschreibung", "Einzelpreis",
                                                   "Gesamtpreis"))
for i in range(len(invoice)):
    print("{:<5d}{:<10d}{:<15}{:<28}{:<10.2f}{:>10.2f}".format(i + 1, invoice[i][0], invoice[i][1], invoice[i][2],
                                                               invoice[i][3], invoice[i][3] * invoice[i][0]))
