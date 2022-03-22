import doctest


def liste_3(max):
    """
    >>> liste_3(10)
    10
    3
    9
    0
    6
    >>> liste_3(2)
    0
    >>> liste_3(7)
    3
    0
    6
    >>> liste_3(18)
    12
    10
    3
    9
    12
    0
    6
    >>> liste_3(5)
    3
    0
    """
    zahlen = [12, 10, 3, 9, 12, 0, 6]
    for zahl in zahlen:
        if zahl <= max:
           print(zahl)


if __name__ == "__main__":
    doctest.testmod()
