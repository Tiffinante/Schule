# Vigenere
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
vigenere_matrix = []

for i in range(26):
    innere_liste = []
    for y in range(26):
        innere_liste.append(alphabet[(y + i) % 26])
    vigenere_matrix.append(innere_liste)


while True:
    while True:
        print("\nSoll Ver- oder Entschlüsselt werden?\n1 Für Verschlüsseln 2 Für Entschlüsseln")
        eingabe = input("1 oder 2 :")
        if not eingabe:
            quit()

        if eingabe.isdecimal():
            eingabe = int(eingabe)
            if 0 < eingabe < 3:
                if eingabe == 1:
                    verschluesseln = True
                    print("Es wird Verschlüsselt")
                    break
                else:
                    verschluesseln = False
                    print("Es wird Entschlüsselt")
                    break

    while True:
        code = input("Code der Entschlüsselt werden soll:")
        if not code:
            quit()

        if code.isalpha():
            code = code.upper()
            if 'Ä' in code or 'Ö' in code or 'Ü' in code:
                print(code)
            else:
                break

    while True:
        key = input("Schlüssel:")
        if not key:
            quit()

        if key.isalpha():
            key = key.upper()
            if 'Ä' in key or 'Ö' in key or 'Ü' in key:
                print(key)
            else:
                break

    # Ver- und Entschlüsselung
    if verschluesseln:
        for i in range(len(code)):
            letter = code[i]
            key_switch = key[i % len(key)]
            hidden_letter = (alphabet.index(letter) + alphabet.index(key_switch)) % 26
            print(alphabet[hidden_letter], end="")
    else:
        for i in range(len(code)):
            hidden_letter = code[i]
            key_switch = key[i % len(key)]
            letter = (alphabet.index(hidden_letter) - alphabet.index(key_switch)) % 26
            print(alphabet[letter], end="")
