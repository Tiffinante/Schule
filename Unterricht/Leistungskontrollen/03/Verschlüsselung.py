# Caesar
alpha = "abcdefghijklmnopqrstuvwxyz".upper()


while True:
    print("Soll Ver- oder Entschlüsselt werden?\n1 Für Verschlüsseln 2 Für Entschlüsseln")
    eingabe = input("1 oder 2 :")
    if not eingabe:
        quit()

    if eingabe.isdecimal():
        eingabe = int(eingabe)
        if 0 < eingabe < 3:
            if eingabe == 1:
                verschleusseln = True
                print("Es wird Verschlüsselt")
                break
            else:
                verschleusseln = False
                print("Es wird Entschlüsselt")
                break

while True:
    code = input("Code:")
    if code.isalpha():
        if code.isupper():
            break


while True:
    verschiebung = input("Um wie viele Stehlen soll Verschoben?\n:")
    if verschiebung.isdecimal():
        verschiebung = int(eingabe)
