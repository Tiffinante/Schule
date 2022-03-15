from FUNCTIONS import *
import time

print()
while True:
    User_name = input(bot_name + ": Wie lautet dein Name?\nDu: ").lower()
    if User_name.isalpha():
        User_name = User_name.title()
        break
    else:
        print(bot_name + ":", "Das Glaube ich nicht!")


# Begrüßung
print(bot_name + ":", "Seid gegrüßt", User_name + "!")
benutzeranleitung()

# Einstiegs Frage
print(bot_name + ": Was willst du über Gaming wissen?")


while True:
    User_question = input("Du: ").lower()
    if not User_question:
        print(ColorCodes.PINK + "System" + ColorCodes.RESET + ": " + ColorCodes.RED + "Sie können mit '!help' die " +
              "Benutzeranleitung aufsuchen oder weiter mit dem Bot schreiben" + ColorCodes.RESET)
    if User_question:
        answer = False

        # Befehle erkennen
        if check_question(User_question):
            continue

        # Satz in wörter zerlegen
        User_words = User_question.split()

        # Antworten
        if "bye" in User_words:
            print(bot_name + ":", f"Ich ünsche dir noch einen Schönen Tag {User_name}.")
            print(ColorCodes.PINK + "System" + ColorCodes.RESET + ": " + ColorCodes.RED + "Bot beendet...")
            quit()

        for element in User_words:
            if element in tags:
                answer = True
                txt = tags.get(element)
                print(bot_name + ":", txt)
                break

        if not answer:
            pass

        # Random Antwort
        if not answer:
            txt = r.choice(random_answers)
            print(bot_name + ":", txt)
