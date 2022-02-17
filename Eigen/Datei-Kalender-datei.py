verlauf = ""


def calendar_build(mon, tue, wed, thr, fri, sat, sun, month_len):
    verlauf = ""
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
        txt = "{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2} ".format(str_mon, str_tue, str_wed, str_thr, str_fri,
                                                                        str_sat, str_sun)
        verlauf += txt + "\n"
        print(txt)
        # calculate the data in the next line
        if loop:
            mon = sun + 1
            tue = mon + 1
            wed = tue + 1
            thr = wed + 1
            fri = thr + 1
            sat = fri + 1
            sun = sat + 1
    return verlauf


months = ("Fehler", 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember')

print('\nHier können sie einen Monat ihrer Wahl anschauen,\ngeben sie dazu zuerst das Jahr und dann den Monat an.\n')
while True:
    print_month = 12
    year = input("Welches Jahr möchten sie sehen? :")
    month = input("Welchen Monat möchten sie sehen? :")
    if year.isdigit() and month.isdigit():
        if year.isdecimal() and month.isdecimal():
            month = int(month)
            year = int(year)
            if 13 > month > 0:
                break

# Invoice for the first day of the month
# Invoice source: https://de.wikipedia.org/wiki/Wochentagsberechnung
if month < 3:
    year -= 1
day = ((1 + int(2.6 * ((month + 9) % 12 + 1) - 0.2) + year % 100 + int(year % 100 / 4) +
        int(year / 400) - 2 * int(year / 100) - 1) % 7 + 7) % 7 + 1
if month < 3:
    year += 1

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

# build of the calendar heading
txt = "\n{:<14}".format(months[month] + " - " + str(year))
verlauf += txt + "\n"
print(txt)
txt = "{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2} ".format("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")
verlauf += txt + "\n"
print(txt)

# check for 30, 31 days or February
if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        verlauf += calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 29)
    else:
        verlauf += calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 28)
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    verlauf += calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 31)
else:
    verlauf += calendar_build(Mon, Tue, Wed, Thr, Fri, Sat, Sun, 30)

with open('Datei-Kalender-datei-verlauf', 'a') as file:
    file.write(verlauf)
