from STATICS import *


def benutzeranleitung():
    print(ColorCodes.UNDERLINE + "\nBenutzeranleitung:" + ColorCodes.RESET)
    print(f'Sie können mit {bot_name} ein Normales Gespräch über Gaming führen.')
    print('Themen in denen sie Trainiert ist, sind Valorant und Minecraft.')
    print('Wenn sie !help eingeben, kommen sie wieder zur Benutzteraleitung.')
    print('Wenn sie !stop oder "Bye" eingeben, wird das Programm Beendet.\n')


def check_question(question: str):
    if question[0] == cmd_signal:
        cmd = question[1:len(question)]
        if cmd == "help":
            benutzeranleitung()
        elif cmd == "stop":
            print(ColorCodes.PINK + "System" + ColorCodes.RESET + ": " + ColorCodes.RED + "Bot beendet...")
            quit()
        else:
            print(ColorCodes.PINK + "System" + ColorCodes.RESET + ": " + ColorCodes.RED + "Kein Gültiger Befehl" +
                  ColorCodes.RESET)
        return True
    else:
        return False
