class ColorCodes:
    GREEN = '\033[92m'  # GREEN
    YELLOW = '\033[93m'  # YELLOW
    RED = '\033[91m'  # RED
    WHITE = '\033[0m'  # WHITE

print('''\nAufgabe 1:

Schreibe ein Programm, welches die Werte von 0 bis 5 ausgibt.''')
for i in range(6):
    print(i)

print('''\nAufgabe 2:

Schreibe ein Programm, welches die Werte von 2 bis 7 ausgibt.''')
for i in range(2,8):
    print(i)

print('''\nAufgabe 3:

Schreibe ein Programm, welches die Werte von 1 bis 19 in Zweierschritten ausgibt.''')
for i in range(1, 21, 2):
    print(i)

print('''\nAufgabe 4:

Schreibe ein Programm, welches die Werte von 10 bis -10 in Zweierschritten rückwärts ausgibt.''')
for i in range(10, -12, -2):
    print(i)
print('''\nAufgabe 5:

Schreibe ein Programm, welches x mit y multipliziert, wobei x von 1 bis 5 läuft und y von 1 bis 3 läuft.''')
for y in range(1, 4):
    for x in range(1, 6):
        print(x * y, end=" ")
    print("")

print('''Aufgabe 6:

Schreibe ein Programm, welches die Nutzerin nach einer Zahl fragt. Anschließend wird
zurückgegeben ob die Zahl durch die Zahl sieben teilbar ist oder nicht. Diese Abfrage wird
solange wiederholt, bis die Nutzerin nichts eingibt (Der Rückgabewert entspricht also einem
leeren String ("").''')

my_list = [0]
for i in my_list:
    my_list.append(i + 1)
    n = input("Number:")
    if n.isdecimal():
        n = int(n)
        if n % 7 == 0:
            print(ColorCodes.GREEN + f"{n} ist durch 7 Teielbar!" + ColorCodes.WHITE)
            break
        else:
            print(ColorCodes.RED + f"{n} ist NICHT durch 7 Teielbar!" + ColorCodes.WHITE)
    else:
        print(ColorCodes.YELLOW + "Bitte nur Zahlen!!!" + ColorCodes.WHITE)
