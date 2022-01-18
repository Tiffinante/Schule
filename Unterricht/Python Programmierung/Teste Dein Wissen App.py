import operator
import random as r

operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def game_wissen(points):

    ops = ("<", ">", "==", "<=", ">=", "!=", "and", "or",)
    boolean = (True, False, "not ", "")
    counter = 1

    print("\nKategorie1: Logische Vergleiche")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))

    while counter < 6:
        number, number2, op = r.randint(1, 3), r.randint(1, 3), ops[r.randint(0, 5)]
        answer = input("{:<5}         {:<25}            {:<1}".format(counter, f"{number} {op} {number2}", ":"))
        if answer.lower() == "t" or answer.lower() == "true" or answer == "1":
            answer = True
        elif answer.lower() == "f" or answer.lower() == "false" or answer == "0":
            answer = False

        if op == "<":
            if (number < number2) == answer:
                points += 1
        elif op == ">":
            if (number > number2) == answer:
                points += 1
        elif op == "==":
            if (number == number2) == answer:
                points += 1
        elif op == "<=":
            if (number <= number2) == answer:
                points += 1
        elif op == ">=":
            if (number >= number2) == answer:
                points += 1
        elif op == "!=":
            if (number != number2) == answer:
                points += 1
        counter += 1

    print("\nKategorie2: Logische Operatoren")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))

    while counter < 11:
        n1, n2, op = boolean[r.randint(2, 3)], boolean[r.randint(2, 3)], ops[r.randint(6, 7)]
        bool1, bool2 = boolean[r.randint(0, 1)], boolean[r.randint(0, 1)]
        answer = input("{:<5}         {:<25}            {:<1}".format(counter, f"{n1}{bool1} {op} {n2}{bool2}", ":"))
        if answer.lower() == "t" or answer.lower() == "true" or answer == "1":
            answer = True
        elif answer.lower() == "f" or answer.lower() == "false" or answer == "0":
            answer = False

        if n1 == "not ":
            if bool1:
                bool1 = False
            else:
                bool1 = True
        if n2 == "not ":
            if bool2:
                bool2 = False
            else:
                bool2 = True

        if op == "and":
            if (bool1 and bool2) == answer:
                points += 1
        elif op == "or":
            if (bool1 or bool2) == answer:
                points += 1
        counter += 1

    print("\nKategorie 3: Logische Operatoren und Vergleiche")
    print("{:<5}         {:<25}            {:<7}".format("Frage", "Bedingung", "Antwort"))

    while counter < 16:
        n1, n2, op = boolean[r.randint(2, 3)], boolean[r.randint(2, 3)], ops[r.randint(6, 7)]
        number, op1, number2 = r.randint(1, 3), ops[r.randint(0, 5)], r.randint(1, 3)
        number_1, op_1, number2_1 = r.randint(1, 3), ops[r.randint(0, 5)], r.randint(1, 3)
        answer = input("{:<5}         {:<25}            {:<1}"
                       .format(counter, f"{n1}{number} {op1} {number2} {op} {n2}{number_1} {op_1} {number2_1}", ":"))
        if answer.lower() == "t" or answer.lower() == "true" or answer == "1":
            answer = True
        elif answer.lower() == "f" or answer.lower() == "false" or answer == "0":
            answer = False

        if op1 == "<":
            bool1 = number_1 < number2_1
        elif op1 == ">":
            bool1 = number_1 > number2_1
        elif op1 == "==":
            bool1 = number_1 == number2_1
        elif op1 == "<=":
            bool1 = number_1 <= number2_1
        elif op1 == ">=":
            bool1 = number_1 >= number2_1
        elif op1 == "!=":
            bool1 = number_1 != number2_1
        else:
            bool1 = ""

        if op_1 == "<":
            bool2 = number_1 < number2_1
        elif op_1 == ">":
            bool2 = number_1 > number2_1
        elif op_1 == "==":
            bool2 = number_1 == number2_1
        elif op_1 == "<=":
            bool2 = number_1 <= number2_1
        elif op_1 == ">=":
            bool2 = number_1 >= number2_1
        elif op_1 == "!=":
            bool2 = number_1 != number2_1
        else:
            bool2 = ""

        if n1 == "not ":
            if bool1:
                bool1 = False
            else:
                bool1 = True
        if n2 == "not ":
            if bool2:
                bool2 = False
            else:
                bool2 = True

        if op == "and":
            if (bool1 and bool2) == answer:
                points += 1
        elif op == "or":
            if (bool1 or bool2) == answer:
                points += 1
        counter += 1

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

    print("\nRanking")
    if punkte_user_1 >= punkte_user_2 >= punkte_user_3:
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
    elif punkte_user_1 >= punkte_user_3 >= punkte_user_2:
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
    elif punkte_user_2 >= punkte_user_1 >= punkte_user_3:
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
    elif punkte_user_2 >= punkte_user_3 >= punkte_user_1:
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
    elif punkte_user_3 >= punkte_user_1 >= punkte_user_2:
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
    else:
        print(f"{user_name3} hat {punkte_user_3} Punkte gesammelt")
        print(f"{user_name2} hat {punkte_user_2} Punkte gesammelt")
        print(f"{user_name1} hat {punkte_user_1} Punkte gesammelt")

    neue_runde = input("\nNeuer Durchgang? j oder n:")
    if neue_runde == "n" or neue_runde == "":
        break
