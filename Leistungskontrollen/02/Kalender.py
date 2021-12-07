"""
Leistungskontrolle 02 Kalender.py
Mika Kattau                 ITA21

Sie können das Jahr und den Monat hintereinander
in die Konsole eingeben, ihnen wird dann ein
Formatierter Kalender des angegebenen Monats im
Angegebenem Jahr ausgegeben. Dies können sie
dauerhaft wiederholen. Um dies zu stoppen,
schreiben die in einen beliebigen Input "stop",
dann wird das Programm automatisch beendet.

-© Mika kattau
"""


def calendar_build(mon, tue, wed, thr, fri, sat, sun, month_len):
    # "Search" for the end of the month and set the remainder to zero.
    loop = True
    while loop:
        if mon == month_len:
            tue, wed, thr, fri, sat, sun = 0, 0, 0, 0, 0, 0
            loop = False
        elif tue == month_len:
            wed, thr, fri, sat, sun = 0, 0, 0, 0, 0
            loop = False
        elif wed == month_len:
            thr, fri, sat, sun = 0, 0, 0, 0
            loop = False
        elif thr == month_len:
            fri, sat, sun = 0, 0, 0
            loop = False
        elif fri == month_len:
            sat, sun = 0, 0
            loop = False
        elif sat == month_len:
            sun = 0
            loop = False
        elif sun == month_len:
            loop = False
        # Insert column of calendar (German = Spalte des Kalenders einsetzen)
        zellen = "| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |.{:.>2}.|.{:.>2}.|" \
            .format(mon, tue, wed, thr, fri, sat, sun)
        print(zellen)
        # calculate the data in the next line
        mon = sun + 1
        tue = mon + 1
        wed = tue + 1
        thr = wed + 1
        fri = thr + 1
        sat = fri + 1
        sun = sat + 1


months = ("Fehler", 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember')
weekday = ("Sonntag", "Montag", "Dinstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")

Mon, Tue, Wed, Thr, Fri, Sat, Sun = "Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"

month_codes = ("Fehler", 6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
# Leap Year Codes. January and February only (German = Schaltjahr-Codes. Nur Januar und Februar)
month_codes_leap_year = ("Fehler", 5, 1)

print('''
Hier kannst du dir einen Monat deiner Wahl anschauen,
gib dazu erst das Jahr und dann den Monat an.
''')

while True:
    print('''
Um das Programm zu beenden, schreibe "stop".
    ''')
    while True:
        start_year = input("Welches Jahr möchtest du sehen? :")
        if start_year == "stop":
            print(" ")
            quit("See you soon ;)")
        start_month = input("Welchen Monat möchtest du sehen? 1 bis 12 :")
        if start_year.isdigit() and start_month.isdigit():
            if start_year.isdecimal() and start_month.isdecimal():
                month = int(start_month)
                year = int(start_year)
                if 13 > month > 0:
                    break
        else:
            if start_month == "stop":
                print(" ")
                quit("bye")

    '''print(months[month])'''

    # Invoice for the first day of the month
    # Invoice source: https://www.youtube.com/watch?v=-EiX7a2SBeA and https://de.wikipedia.org/wiki/Wochentagsberechnung
    year_code = ((year % 100 / 4) + year % 100) % 7

    # Determination and adaptation for centuries (German = Bestimmung und anpassung für die jahunderte)
    if 1699 < year < 1800:
        year_code += 5
    elif 1799 < year < 1900:
        year_code += 3
    elif 1899 < year < 2000:
        year_code += 1
    elif 1999 < year < 2100:
        year_code += 0
        # to recognize the pattern (German = um das Muster zu erkennen)
    elif 2099 < year < 2200:
        year_code += 5

    # Query about a leap year
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month < 3:
        # Calculation of the day with leap year
        day = (1 + month_codes_leap_year[month] + year_code) % 7
    else:
        # Calculation of the day without leap year
        day = (1 + month_codes[month] + year_code) % 7
    # Round off the number and take the day from the Tuple
    day = int(day)
    print(" ")

    '''
    # Arithmetic verification (German = Rechenüberprüfung)
    print(day)
    print(weekdays[tag])
    '''

    # calendar
    print(f"{months[month]} - {year}")
    print("| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"))

    # Insert of the first day and days after
    if day == 1:
        Tue, Wed, Thr, Fri, Sat, Sun = 2, 3, 4, 5, 6, 7
        Mon = 1
    elif day == 2:
        Mon, Wed, Thr, Fri, Sat, Sun = 0, 2, 3, 4, 5, 6
        Tue = 1
    elif day == 3:
        Mon, Tue, Thr, Fri, Sat, Sun = 0, 0, 2, 3, 4, 5
        Wed = 1
    elif day == 4:
        Mon, Tue, Wed, Fri, Sat, Sun = 0, 0, 0, 2, 3, 4
        Thr = 1
    elif day == 5:
        Mon, Tue, Wed, Thr, Sat, Sun = 0, 0, 0, 0, 2, 3
        Fri = 1
    elif day == 6:
        Mon, Tue, Wed, Thr, Fri, Sun = 0, 0, 0, 0, 0, 2
        Sat = 1
    elif day == 0 or 7:
        Mon, Tue, Wed, Thr, Fri, Sat = 0, 0, 0, 0, 0, 0
        Sun = 1

    # check for 30, 31 days or February
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 29)
        else:
            calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 28)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 31)
    else:
        calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 30)
