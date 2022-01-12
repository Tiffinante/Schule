
print("number 1 / number 2")
while True:
    try:
        n1 = int(input("number 1: "))
        n2 = int(input("number 2: "))
        n = n1 / n2
    except ZeroDivisionError as e:
        # e ist der Error der ausgegeben wird als Variable
        print(e)
        print("Du kannst nicht durch 0 Teilen")
    except ValueError as error:
        print(error)
        print("Bitte nur Zahlen")
    except OverflowError as error:
        print(error)

    except Exception as error:
        print(error)
        print("Alle anderen Fehler die auftreten können")

    else:
        # wenn kein Fehler auftritt
        print(n)
        break
    finally:
        print("-" * 70)
        print("Das wird immer ausgefürt nützlich um datein zu schliesen oder so")