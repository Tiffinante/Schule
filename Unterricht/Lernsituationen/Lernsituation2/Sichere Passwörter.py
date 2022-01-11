import random


class ColorCodes:
    GOOD = '\033[92m'  # GREEN
    WEEK = '\033[93m'  # YELLOW
    BAD = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR WHITE


letter_upper = 0
letter_lower = 0
letter_digit = 0
letter_special = 0

fail_count = 0

# "set" damit nichts 2x überprüft wird
# set toopel liste
passwoerter = {"123456", "123456789", "12345678", "passw0rd", "passw0rt", "password", "passwort", "1234567", "123123",
               "1234567890", "111111", "abc123", "00000", "123", "abc", "000000123456", "123456789", "password",
               "adobe123", "12345678", "qwerty", "1234567", "111111", "photoshop", "123123", "1234567890", "000000",
               "abc123", "1234", "adobe1", "macromedia", "azerty", "iloveyou", "aaaaaa", "654321", "12345", "666666",
               "sunshine", "123321", "letmein", "monkey", "asdfgh", "password1", "shadow", "princess", "dragon",
               "adobeadobe", "daniel", "computer", "drowssap ", "michael", "121212", "charlie", "master", "superman",
               "qwertyuiop", "112233", "asdfasdf", "jessica", "1q2w3e4r", "welcome", "1qaz2wsx", "987654321", "fdsa",
               "753951", "chocolate", "fuckyou", "soccer", "tigger", "asdasd", "thomas", "asdfghjkl", "internet",
               "michelle", "football", "123qwe", "zxcvbnm", "dreamweaver", "7777777", "maggie", "qazwsx", "baseball",
               "jennifer", "jordan", "abcd1234", "trustno1", "buster", "555555", "liverpool", "abc", "whatever",
               "11111111", "102030", "123123123", "andrea", "pepper", "nicole", "killer", "abcdef", "hannah", "test",
               "alexander", "andrew", "222222", "joshua", "freedom", "samsung", "asdfghj", "purple", "ginger", "123654",
               "matrix", "secret", "summer", "1q2w3e", "snoopy1"}

while True:
    password = input("passwort:")
    if password.lower() == "penis":
        print(ColorCodes.BAD + "ACHTUNG! Ihr Passwort ist zu kurts!" + ColorCodes.RESET)
    elif not (" " in password) and password.isprintable():
        print("")
        break
    else:
        print("Bitte verwenden sie keine Lehrzeichen und nur zeichen die 'räguler' verwendbar sind")
# password = "&Mein 1PasswOrt23!"
for letter in password:
    if letter.isdigit():
        letter_digit += 1
    elif letter.isupper():
        letter_upper += 1
    elif letter.islower():
        letter_lower += 1
    else:
        letter_special += 1

password_len = len(password)

for i in passwoerter:
    if i in password or i == password:
        fail_count += 1
        print("Verwenden sie ein eigenes Password")
        break
if letter_lower < 2:
    fail_count += 1
    print("Verwenden sie (mehr) kleine Buchstaben")
if letter_upper < 3:
    fail_count += 1
    print("Verwenden sie (mehr) Große Buchstaben")
if letter_digit < 4:
    fail_count += 1
    print("Verwenden sie (mehr) Zahlen")
if letter_special < 3:
    fail_count += 1
    print("Verwenden sie (mehr) Sonderzeichen")

if password.istitle():
    fail_count += 1
    print("Verwenden sie Keine Wortähnlichen buchstaben ketten")
if password.isalnum():
    fail_count += 1
    print("Verwenden sie keine reinfolge wie 'abc' oder '123'")

if password_len < 10:
    fail_count += 1
    print("Verwenden sie ein längeresw passwort")

print(fail_count)

if fail_count >= 5:
    print(ColorCodes.BAD + "\nACHTUNG! Ihr Passwort ist SEHR Schlecht" + ColorCodes.RESET)
elif fail_count >= 3:
    print(ColorCodes.WEEK + "\nAchtung! Ihr Passwort ist Schwach" + ColorCodes.RESET)
elif fail_count >= 1:
    print(ColorCodes.GOOD + "\nIhr Passwort ist Sicher" + ColorCodes.RESET)
elif fail_count == 0:
    print(ColorCodes.GOOD + "\nIhr Passwort ist SEHR Sicher" + ColorCodes.RESET)

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()|=?'<>,.;:-_#+*@€{[]}"
password = ""
for i in range(30):
    password = password + alphabet[random.randrange(len(alphabet))]
print("\nEin Password von uns für sie:")
print(password)
