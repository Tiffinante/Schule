"""
mehr als 10 zeichen
Groß klein buchstaben
Sonderzeichen
Zahlen
Keine reinfolgen wie abc oder 123 ...
keine Worte oder Jahre
"""
import random


class ColorCodes:
    GOOD = '\033[92m'  # GREEN
    WEEK = '\033[93m'  # YELLOW
    BAD = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR WHITE


passwoerter = ("123456", "123456789", "12345678", "passw0rd", "passw0rt", "password", "passwort", "1234567", "123123",
               "1234567890", "111111", "abc123", "00000", "123")

letter_alpha = 0
letter_upper = 0
letter_lower = 0
letter_digit = 0
letter_special = 0

password = input("passwort:")
# password = "&Mein 1PasswOrt23!"
for letter in password:
    if letter.isalpha():
        letter_alpha += 1
        if letter.lower():
            letter_lower += 1
        if letter.isupper():
            letter_upper += 1
    elif letter.isdigit():
        letter_digit += 1
    else:
        letter_special += 4

letter_lower = letter_lower - letter_upper
password_len = len(password)
print(letter_alpha, letter_upper, letter_lower, letter_digit, letter_special, password_len)

if letter_lower > letter_upper:
    letter_ul = (letter_lower - letter_upper) // 4
elif letter_upper > letter_lower:
    letter_ul = (letter_upper - letter_lower) // 4
else:
    letter_ul = 5
print(letter_ul)

if letter_digit == 0:
    print("Verwenden sie auch Zahlen")
if letter_lower == 0:
    print("Verwenden sie auch Kleine Buchstaben")
    security = 0
if letter_upper == 0:
    print("Verwenden sie auch Große Buchstaben")
    security = 0
if password.isspace() or password == "":
    print("Ihr passwort sollte Zeichen beinhalten!")
    security = 0
if password_len < 10:
    print("Ihr Passwort sollte min. 10 zeichen haben!")
    security = 0
if password.lower() in passwoerter:
    print("Ihr Passwort existirt in einer Liste aus dem internet!")
    security = 0
elif password.istitle():
    print("Bitte Achten sie darauf Gruß und klein buchstaben zu mischen!")
    security = (letter_alpha + letter_ul + letter_digit) - password_len
else:
    security = letter_alpha + letter_ul + letter_digit + (password_len // 4)
print(f"\nSecurity level: {security}")

if password.lower() == "penis":
    print(ColorCodes.BAD + "ACHTUNG! Ihr Passwort ist zu kurts!" + ColorCodes.RESET)
elif security >= 8:
    if security >= 16:
        print(ColorCodes.GOOD + "Ihr Passwort ist Sicher" + ColorCodes.RESET)
    else:
        print(ColorCodes.WEEK + "Achtung! Ihr Passwort ist Schwach" + ColorCodes.RESET)
else:
    print(ColorCodes.BAD + "ACHTUNG! Ihr Passwort ist SEHR Schlecht" + ColorCodes.RESET)

if password_len >= 100:
    print(ColorCodes.BAD + "Gut David Sehr GUT!" + ColorCodes.RESET)

answer = ""
if security <= 8:
    print("\nWir würden sie dringend darum bitten ein anderes Passwort zu Verweden! \n"
          "Wenn sie sich keins infalln lassen können, Verwenden sie unser generirtes.")
    answer = "y"
elif security <= 12:
    print("\nIhr passwort ist nur gerade so durch den Test gekommen, \n"
          "Wir würden sie darum bitten eins von uns generirtes Passwort zu Verwenden!")
    answer = "y"
elif security < 16:
    print("\nWir würden ihnen Wärmstenst ein neues passwort empfehlen. \n"
          "Wenn sie also ein Neues haben wollen können sie es hier Generieren lassen.")
elif security < 25:
    print("\nAuch wenn ihr Passwort den Test bestanden hatt ist es dennoch nicht Perfekt. \n"
          "Sie können sich von uns hier ein Passwort generiren lassen wenn sie möchten.")
elif security > 25:
    print("\nEigentlich brauchen sie kein Neues Passwort, \n"
          "aber wenn ihr Logischer Menschen verstand ihnen sagt das sie ein Neues brauchen, \n"
          "können sie hier eins generieren lassen.")

if answer != "y":
    answer = input("\nMöchten sie ein neues Passwort von uns? y oder n:")
    if answer != "y":
        if security < 16:
            print("ihre wahl sir...")
            quit("Programm beendet")
        elif security < 25:
            print("Wenn ihre daten nicht so wichtig sind...")
            quit("Programm beendet")
        elif security > 25:
            print("ist auch okay :)")
            quit("Programm beendet")

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()|=?'<>,.;:-_#+*@€{[]}"
password = ""

for i in range(30):
    password = password + alphabet[random.randrange(len(alphabet))]

print("\nPassword")
print(password)
