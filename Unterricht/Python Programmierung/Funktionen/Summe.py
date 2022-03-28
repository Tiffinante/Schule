import time


def input_integer(question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt.
    :param question: Text für den Input
    :return: User Input
    """
    while True:
        n = input(question)
        if n.isdecimal():
            return int(n)


def sum_from_to(start: int, end: int) -> int:
    """
    Rechnet alle zahlen zur summe zwischen zwei Zahlen die Inklusiv sind.
    Beispiel:
        start = 1
        end = 3
        1 + 2 + 3 = 6
    :param start: Erste Zahl als int
    :param end: Letzte Zahl als int
    :return: Summe als int
    """
    sum_of = end
    for i in range(start, end):
        sum_of += i
    return sum_of


def print_summ(start, end, sum_of) -> None:
    """
    Printet den Folgenden satz:
        Die Summe der Zahlen von " + str(start) + " bis " + str(end) + " lautet: " + str(summe)
    :param start: Erste Zahl
    :param end: Letzte Zahl
    :param sum_of: summe zwischen den Zahlen
    :return: None
    """
    print("Die Summe der Zahlen von " + str(start) + " bis " + str(end) + " lautet: " + str(sum_of))


start_time = time.time()

anfang = input_integer("Nennen Sie den Summenanfang: ")
ende = input_integer("Nennen Sie den Summenanfang: ")
summe = sum_from_to(anfang, ende)
print_summ(anfang, ende, summe)

print("--- %s seconds ---" % (time.time() - start_time))
