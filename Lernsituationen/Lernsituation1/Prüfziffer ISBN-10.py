import time
from random import randint


def random_number(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


print('''
                ##################################
                ##      ISBN-Nummernprüfer      ##
                ##         by Mika              ##
                ##################################


Gib eine 9 oder 10 Stellige Isbn nummer ein
Die 10 stellige wird geprüft die 9 stellige ausgerechnet
''')

answer = ""
while not (answer == "stop"):
    isbn = 0  # 3826604237
    while not (len(str(isbn))) == 9 and not (len(str(isbn)) == 10) and not (isbn == "stop") and not (isbn == "help"):
        while True:
            print("Bitte eine 9 oder 10 stellige nummer!")
            isbn = input("Die isbn nummer:")
            if isbn.isdecimal():
                isbn = int(isbn)
                break
            else:
                if isbn == "stop":
                    print(" ")
                    time.sleep(0.1)
                    quit("Programm wird beendet...(0)")
                elif isbn == "help":
                    print(" ")
                    print("Gib eine 9 oder 10 Stellige Isbn nummer ein")
                    print("Die 10 stellige wird geprüft die 9 stellige ausgerechnet")
                    print('Du kannst jederzeit "stop" oder "help" benutzen.')
                    print(" ")
                else:
                    print(" ")
                    print("Bitte nur Zahlen!!!")

    # Ausrechnen der prüfziffer
    if len(str(isbn)) == 9:
        print(" ")
        print("Prüfziffer wird berechnet...")
        print(" ")

        x = 1
        y = 100000000
        number = 0
        while x < 10:
            number += x * ((isbn // y) % 10)
            x += 1
            y //= 10
        number %= 11

        print("Die Prüfziffer ist", number)
        print("Die ganze zahl lautet", str(isbn) + str(number))

    # Prüfen der Prüfnummer
    if len(str(isbn)) == 10:
        print(" ")
        print("Prüfen der Prüfziffer...")
        print(" ")

        x = 1
        y = 1000000000
        number = 0
        while x < 10:
            number += x * ((isbn // y) % 10)
            x += 1
            y //= 10
        number %= 11

        if ((isbn // 1) % 10) == number:
            print('Die isbn "', isbn, '" ist richtig')
            print(" ")
        else:
            print('Die isbn "', isbn, '" ist NICHT richtig')
            print("Die passende Prüfziffer währe ", number)
            print(" ")

    print("Möchtest du eine random isbn nummer erhalten?")
    print("Antworte mit yes(y) oder no()n")

    # Fragen nach Random nummer
    answer = "idk"
    while not (answer == "y") and not (answer == "n") and not (answer == "stop") and not (answer == "help"):
        answer = str(input("y or n:"))

    if answer == "y":
        isbn = random_number(9)

        x = 1
        y = 100000000
        number = 0
        while x < 10:
            number += x * ((isbn // y) % 10)
            x += 1
            y //= 10
        number %= 11

        isbn = str(isbn) + str(number)
        if ((int(isbn) // 1) % 10) == number:
            print(" ")
            print('Die isbn lautet:', isbn)
            print(" ")
        else:
            print(" ")
            time.sleep(0.1)
            quit("Fehler bei erstellen der nummer...(1)")

    if answer == "n":
        print(" ")

    if answer == "help":
        print(" ")
        print('Du kannst "y" für ja benutzen und "n" für nein')
        print('um eine Zufällige nummer zu generieren')
        print(" ")
        print('Du kannst jederzeit "stop" oder "help" benutzen.')
        print(" ")

    if answer == "stop":
        print(" ")
        time.sleep(0.1)
        quit("Programm wird beendet...(2)")

time.sleep(0.1)
quit("Programm wird beendet...(3)")
