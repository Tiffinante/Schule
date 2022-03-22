import doctest


def liste_4(min, max):
    """
    >>> liste_4(1, 3)
    1
    4
    9
    >>> liste_4(2, 5)
    4
    9
    16
    25
    >>> liste_4(5, 10)
    25
    36
    49
    64
    81
    100
    >>> liste_4(9, 12)
    81
    100
    121
    144
    """
    zahlen = []
    for i in range(min, max + 1):
        zahlen.append(i*i)

    for zahl in zahlen:
        print(zahl)


if __name__ == "__main__":
    doctest.testmod()
