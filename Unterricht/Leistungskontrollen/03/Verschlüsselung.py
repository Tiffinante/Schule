# Caesar
alpha = "abcdefghijklmnopqrstuvwxyz".upper()

while True:
    while True:
        print("\nSoll Ver- oder Entschlüsselt werden?\n1 Für Verschlüsseln 2 Für Entschlüsseln")
        eingabe = input("1 oder 2 :") # 1 = Verschlüsseln 2 = Entschlüssln
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

    while True: # Code Eingeben
        if not eingabe:
            quit()

        code = input("Code:")
        if code.isalpha():
            if code.isupper():
                break

    while True: # Um wie viele stellen das Verschoben werden
        if not eingabe:
            quit()

        verschiebung = input("Um wie viele Stehlen soll Verschoben?\n:")
        if verschiebung.isdecimal():
            verschiebung = int(verschiebung)
            if 1 < verschiebung < 26:
                break

    print()

    if verschleusseln: # Verschlüsseln
        for element in code:
            if alpha.index(element) + verschiebung >= 26:
                print(alpha[(alpha.index(element) + verschiebung) - 26], end="")
            else:
                print(alpha[alpha.index(element) + verschiebung], end="")
    else: # Entschlüsseln
        for element in code:
            print(alpha[alpha.index(element) - verschiebung], end="")

    print()