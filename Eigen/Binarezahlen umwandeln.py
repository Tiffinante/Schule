import time


print("Sie konnen eine Dezimalzahl in binare ausgeben lassen und anders herrum.")
print('"b" wenn sie eine binare zahl haben, "d" wenn sie eine Dezimal zahl haben.')

error = False
start = "start"
while not(start == "stop"):
    print(" ")
    print('Sie können auch "help" oder "stop" benutzen')
    print(" ")

    answer = "idk"
    while not(answer == "b") and not(answer == "d") and not(answer == "help") and not(answer == "stop"):
        answer = str(input('d oder b:'))

    if answer == "help":
        print(" ")
        print("Sie konnen eine Dezimalzahl in binare ausgeben lassen und anders herrum.")
        print('"b" wenn sie eine binare zahl haben, "d" wenn sie eine Dezimal zahl haben.')

    if answer == "d":
        list1 = []

        print("")
        dezimalzahl = int(input("Ihre Dezimalzahl:"))

        while dezimalzahl > 0:
            zwischen_Summe = dezimalzahl % 2
            list1.insert(0, zwischen_Summe)
            dezimalzahl //= 2
        s = ""
        for nr in list1:
            s += str(nr)
        ergebniss = int(s)
        print(ergebniss)

    if answer == "b":
        print(" ")
        binaerzahl = str(input("Ihre Binärzahl:"))
        binaerzahl_int = int(binaerzahl)

        ergebnis = 0
        multiplikator = 1

        while len(binaerzahl) > 0:
            len_binaer = len(binaerzahl) - 1
            stelle = binaerzahl[len_binaer]

            if stelle == "1":
                ergebnis += multiplikator
                multiplikator *= 2
                binaerzahl = binaerzahl[:-1]

            elif stelle == "0":
                multiplikator *= 2
                binaerzahl = binaerzahl[:-1]

            else:
                print(" ")
                print("Keine Gültige zahl")
                binaerzahl = ""
                error = True

        if error:
            print(" ")
            error = 0
        else:
            print("die binärzahl", binaerzahl_int, "ist:", ergebnis)

    if answer == "stop":
        print(" ")
        time.sleep(0.5)
        quit("Programm stoppt...")

print(" ")
time.sleep(0.5)
quit("Fehler beim wiederholen der Frage...")
