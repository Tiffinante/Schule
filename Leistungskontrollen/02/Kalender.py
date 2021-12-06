import math

months = ["Fehler", 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember', ]
wochentage = ["Sonntag", "Montag", "Dinstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

monats_codes = {
    1: 6,
    2: 2,
    3: 2,
    4: 5,
    5: 0,
    6: 3,
    7: 5,
    8: 1,
    9: 4,
    10: 6,
    11: 2,
    12: 4,
}
monats_s_codes = {  # Codes für schaldjahre. Nur Januar und Februar
    1: 5,
    2: 1,

}

while True:
    start_jahr = input("Welches Jahr möchtest du sehen? :")
    start_monat = input("Welchen Monat möchtest du sehen? 1 bis 12 :")
    if start_jahr.isdigit() and start_monat.isdigit():
        if start_jahr.isdecimal() and start_monat.isdecimal():
            monat = int(start_monat)
            jahr = int(start_jahr)
            if 13 > monat > 0:
                break

print(months[monat])

# Rechnung für ersten Tag im Monat
# Rechnungs Quelle: https://www.youtube.com/watch?v=-EiX7a2SBeA
jahres_code = ((jahr % 100 / 4) + jahr % 100) % 7
# Abfrage nach einem schaldjahr
if (jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0) and monat < 3:
    # Berechnung des Tages mit schaltjahr
    tag = (1 + monats_s_codes.get(monat) + jahres_code) % 7
else:
    # Berechnung des Tages
    tag = (1 + monats_codes.get(monat) + jahres_code) % 7
# Abrunden der Zahl und Tag aus der Liste entnehmen
print(tag)
print(wochentage[math.floor(tag)])

# Kalender
print(" ")
print(f"{months[monat]} - {jahr}")
tageszeile = "|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")
print(tageszeile)
# 30 oder 31 tage oder Februar
if monat == 2:
    if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
        # 29 Tage
        datezeile = "|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format("x", "x", "x", "x", "x", "x", "x")
        print(datezeile)
    else:
        # 28 Tage
        datezeile = "|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format("x", "x", "x", "x", "x", "x", "x")
        print(datezeile)
elif monat == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    # 31 Tage
    datezeile = "|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format("x", "x", "x", "x", "x", "x", "x")
    print(datezeile)
else:
    # 30 Tage
    datezeile = "|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format("x", "x", "x", "x", "x", "x", "x")
    print(datezeile)
