import math

months = ["Fehler", 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember', ]

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

julianischer_monat = ["Fehler", 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = julianischer_monat[monat]
d = 1
c = jahr // 100
y = jahr % 100

w = (d + (2.6 * m - 0.2) + y + (y / 4) + (c / 4) - 2 * c) % 7
print(math.ceil(w)) # rundet nach oben floor rundet nach unten
