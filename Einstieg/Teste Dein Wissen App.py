import operator
import random as r

operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def game_wissen(points):

    operator = ("<", ">", "==", "<=", ">=", "!=", "and", "or",)
    boolean = ("True", "False")

    print("\nKategorie1: Logische Vergleiche")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))

    counter = 0
    while counter < 5:
        number, op, number2 = r.randint(1, 3), operator[r.randint(0, 5)], r.randint(1, 3)
        answer = input("{:<5}         {:<25}            {:<1}".format("1", f"{number} {op} {number2}", ":"))
        if answer.lower() == "t" or answer.lower() == "true" or answer == "1":
            answer = True
        elif answer.lower() == "f" or answer.lower() == "false" or answer == "0":
            answer = False

        if op == "<":
            check_answer = number < number2
            if check_answer == answer:
                points += 1
        elif op == ">":
            pass
        elif op == "==":
            pass
        elif op == "<=":
            pass
        elif op == ">=":
            pass
        elif op == "!=":
            pass
        counter += 1

    print("\nKategorie2: Logische Operatoren")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))
    kategorie2_1 = input("{:<5}         {:<25}            {:<1}".format("6", "not False or not True", ":"))
    kategorie2_2 = input("{:<5}         {:<25}            {:<1}".format("7", "True and not True", ":"))
    kategorie2_3 = input("{:<5}         {:<25}            {:<1}".format("8", "False or not True", ":"))
    kategorie2_4 = input("{:<5}         {:<25}            {:<1}".format("9", "False and not False", ":"))
    kategorie2_5 = input("{:<5}         {:<25}            {:<1}".format("10", "not False or True", ":"))
    if kategorie2_1.lower() == "t" or kategorie1_1.lower() == "true" or kategorie2_1.lower() == "1":
        points += 1
    if kategorie2_2.lower() == "f" or kategorie2_2.lower() == "false" or kategorie2_2.lower() == "0":
        points += 1
    if kategorie2_3.lower() == "f" or kategorie2_3.lower() == "false" or kategorie2_3.lower() == "0":
        points += 1
    if kategorie2_4.lower() == "f" or kategorie2_4.lower() == "false" or kategorie2_4.lower() == "0":
        points += 1
    if kategorie2_5.lower() == "t" or kategorie2_5.lower() == "true" or kategorie2_5.lower() == "1":
        points += 1

    print("\nKategorie 3: Logische Operatoren und Vergleiche")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))
    kategorie3_1 = input("{:<5}         {:<25}            {:<1}".format("11", "1 < 3 or 1 < 3", ":"))
    kategorie3_2 = input("{:<5}         {:<25}            {:<1}".format("12", "3 < 1 and not 1 < 2", ":"))
    kategorie3_3 = input("{:<5}         {:<25}            {:<1}".format("13", "not 1 < 2 and not 1 < 3", ":"))
    kategorie3_4 = input("{:<5}         {:<25}            {:<1}".format("14", "2 < 1 and not 2 < 3", ":"))
    kategorie3_5 = input("{:<5}         {:<25}            {:<1}".format("15", "2 < 3 and 2 < 2", ":"))
    if kategorie3_1.lower() == "t" or kategorie1_1.lower() == "true" or kategorie3_1.lower() == "1":
        points += 1
    if kategorie3_2.lower() == "f" or kategorie3_2.lower() == "false" or kategorie3_2.lower() == "0":
        points += 1
    if kategorie3_3.lower() == "f" or kategorie3_3.lower() == "false" or kategorie3_3.lower() == "0":
        points += 1
    if kategorie3_4.lower() == "f" or kategorie3_4.lower() == "false" or kategorie3_4.lower() == "0":
        points += 1
    if kategorie3_5.lower() == "f" or kategorie3_5.lower() == "false" or kategorie3_5.lower() == "0":
        points += 1

    return points


while True:
    user_name1 = input("\nDein Name:")
    punkte = 0
    punkte_user_1 = game_wissen(punkte)
    user_name2 = input("\nDein Name:")
    punkte = 0
    punkte_user_2 = game_wissen(punkte)
    user_name3 = input("\nDein Name:")
    punkte = 0
    punkte_user_3 = game_wissen(punkte)

    print("\nErgebnisse")

    print("\nRanking")
    if punkte_user_1 > punkte_user_2 > punkte_user_3:
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
    elif punkte_user_1 > punkte_user_3 > punkte_user_2:
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
    elif punkte_user_2 > punkte_user_1 > punkte_user_3:
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
    elif punkte_user_2 > punkte_user_3 > punkte_user_1:
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
    elif punkte_user_3 > punkte_user_1 > punkte_user_2:
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
    else:
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")

    neue_runde = input("Neuer Durchgang? j oder n:")
    if neue_runde == "n":
        break
