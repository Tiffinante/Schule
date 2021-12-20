"""
mehr als 10 zeichen
    bis 7 rot
    bis 15 Gelb
    dann Grün
Groß klein buchstaben
Sonderzeichen
Zahlen
Keine reinfolgen wie abc oder 123 ...
keine Worte oder Jahre
Umlaute

"""

class colors:
    GOOD = '\033[92m'  # GREEN
    WEEK = '\033[93m'  # YELLOW
    BAD = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR WHITE

password = input("passwort:")
# password = "&Mein 1PasswOrt23!"
for i in password:
    print(i)


print(colors.GOOD + "Ihr Passwort ist Sicher" + colors.RESET)
print(colors.WEEK + "Achtung! Ihr Passwort ist Schwach" + colors.RESET)
print(colors.BAD + "ACHTUNG! Ihr Passwort ist SEHR Schlecht" + colors.RESET)


