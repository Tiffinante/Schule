"""
Leistungskontrolle 02 Kalender.py
Mika Kattau                 ITA21

Sie können das Jahr und den Monat hintereinander
in die Konsole eingeben, ihnen wird dann ein
Formatierter Kalender des angegebenen Monats im
Angegebenem Jahr ausgegeben. Dies können sie
dauerhaft wiederholen. Um dies zu stoppen,
schreiben sie in einen beliebigen Input "stop",
dann wird das Programm automatisch beendet.

Für besonders vor rausplanende Menschen kann man
auch anstatt einem Monat "alle" schreiben,
dann wird einem Januar bis Dezember ausgegeben.

Getestet mit https://chroniknet.de/extra/welcher-wochentag-war-der/?datum=7.12.1935

-© Mika kattau
"""


def calendar_build(mon, tue, wed, thr, fri, sat, sun, month_len):
    loop = True
    while loop:
        # "Search" for the end of the month and set the remainder to "".
        if mon == month_len:
            tue, wed, thr, fri, sat, sun = "", "", "", "", "", ""
            loop = False
        elif tue == month_len:
            wed, thr, fri, sat, sun = "", "", "", "", ""
            loop = False
        elif wed == month_len:
            thr, fri, sat, sun = "", "", "", ""
            loop = False
        elif thr == month_len:
            fri, sat, sun = "", "", ""
            loop = False
        elif fri == month_len:
            sat, sun = "", ""
            loop = False
        elif sat == month_len:
            sun = ""
            loop = False
        elif sun == month_len:
            loop = False
        # Insert column of calendar (German = Spalte des Kalenders einsetzen)
        str_mon, str_tue, str_wed, str_thr, str_fri, str_sat, str_sun = \
            str(mon), str(tue), str(wed), str(thr), str(fri), str(sat), str(sun)
        lines = "| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |.{:.>2}.|.{:.>2}.|" \
            .format(str_mon, str_tue, str_wed, str_thr, str_fri, str_sat, str_sun)
        print(lines)
        # calculate the data in the next line
        if loop:
            mon = sun + 1
            tue = mon + 1
            wed = tue + 1
            thr = wed + 1
            fri = thr + 1
            sat = fri + 1
            sun = sat + 1


months = ("Fehler", 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember')

months_digits = {'januar': "1", 'februar': "2", 'märz': "3", 'april': "4", 'mai': "5", 'juni': "6", 'juli': "7",
                 'august': "8", 'september': "9", 'oktober': "10", 'november': "11", 'dezember': "12"}

print('\nHier kannst du dir einen Monat deiner Wahl anschauen,\ngib dazu erst das Jahr und dann den Monat an.')

while True:
    print('\nUm das Programm zu beenden, schreibe "stop".\n')
    while True:
        print_month = 12
        year = input("Welches Jahr möchten sie sehen? :")
        if year == "stop":
            quit("\nSee you soon ;)")
        month = input("Welchen Monat möchten sie sehen? Es gehen auch alle:")
        if not (month.isdigit()):
            # allows you to write the month in letters
            if month.lower() in months_digits:
                month = months_digits.get(month.lower())
            # allows you to show you all the months of the year at once
            elif month == "all" or month == "alle":
                month = "1"
                print_month = 1
            elif month == "stop":
                quit("\nbye")
        if year.isdigit():
            if year.isdecimal() and month.isdecimal():
                month = int(month)
                year = int(year)
                if 13 > month > 0:
                    break

    # check for a leap year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    while print_month < 13:
        # Invoice for the first day of the month
        # Invoice source: https://de.wikipedia.org/wiki/Wochentagsberechnung
        if month < 3:
            year -= 1
        day = ((1 + int(2.6 * ((month + 9) % 12 + 1) - 0.2) + year % 100 + int(year % 100 / 4) +
                int(year / 400) - 2 * int(year / 100) - 1) % 7 + 7) % 7 + 1
        if month < 3:
            year += 1

        # build of the calendar heading
        top = months[month] + " - " + str(year)
        if leap_year:
            print("\n{:<14}{:>22}".format(top, "Ein Schaltjahr"))
        else:
            print("\n{:<14}".format(top))
        print("| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format("Mo", "Di", "Mi", "Do", "Fr", "Sa",
                                                                                 "So"))

        # Insert of the first day and days after
        if day == 1:
            Tue, Wed, Thr, Fri, Sat, Sun = 2, 3, 4, 5, 6, 7
            Mon = 1
        elif day == 2:
            Mon, Wed, Thr, Fri, Sat, Sun = "", 2, 3, 4, 5, 6
            Tue = 1
        elif day == 3:
            Mon, Tue, Thr, Fri, Sat, Sun = "", "", 2, 3, 4, 5
            Wed = 1
        elif day == 4:
            Mon, Tue, Wed, Fri, Sat, Sun = "", "", "", 2, 3, 4
            Thr = 1
        elif day == 5:
            Mon, Tue, Wed, Thr, Sat, Sun = "", "", "", "", 2, 3
            Fri = 1
        elif day == 6:
            Mon, Tue, Wed, Thr, Fri, Sun = "", "", "", "", "", 2
            Sat = 1
        # 0 or 7:
        else:
            Mon, Tue, Wed, Thr, Fri, Sat = "", "", "", "", "", ""
            Sun = 1

        # check for 30, 31 days or February
        if month == 2:
            if leap_year:
                calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 29)
            else:
                calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 28)
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 31)
        else:
            calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 30)

        if print_month < 12:
            month += 1
        print_month += 1
