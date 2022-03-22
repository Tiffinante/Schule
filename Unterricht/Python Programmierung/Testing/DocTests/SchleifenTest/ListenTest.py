import doctest


def liste_1():
    """
    >>> liste_1()
    3
    5
    9
    9
    """
    zahlen = [3, 5, 7, 9]
    zahl = zahlen[0]
    print(zahl)
    zahl2 = zahlen[1]
    print(zahl2)
    zahl3 = zahlen[3]
    print(zahl3)
    zahl4 = zahlen[-1]
    print(zahl4)


if __name__ == "__main__":
    doctest.testmod()
