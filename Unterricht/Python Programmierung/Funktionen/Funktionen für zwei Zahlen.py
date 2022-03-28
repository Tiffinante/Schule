def input_integer(question: str) -> int:
    while True:
        n = input(question)
        if n.isdecimal():
            return int(n)


def mittelwert_a_b(a: int, b: int) -> float:
    return (a + b) / 2


def maxwert_a_b(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


def minwert_a_b(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b


def absoluter_abstand_a_b(a: int, b: int) -> int:
    if a < b:
        return b - a
    else:
        return a - b


def ggt_of_a_b(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        while b != 0:
            if a < b:
                b = b - a
            else:
                a = a - b
    return a


first = input_integer("a: ")
second = input_integer("b: ")

print("\nMittlwert:", mittelwert_a_b(first, second))
print("Maxwert:", maxwert_a_b(first, second))
print("Minwert:", minwert_a_b(first, second))
print("absoluter abstand:", absoluter_abstand_a_b(first, second))
print("größter gemeinsamer Teiler", ggt_of_a_b(first, second))
