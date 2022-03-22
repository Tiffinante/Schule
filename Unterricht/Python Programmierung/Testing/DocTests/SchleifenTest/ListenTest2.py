import doctest


def liste_2(index):
    """
    >>> liste_2(0)
    2
    >>> liste_2(-1)
    12
    >>> liste_2(-2)
    10
    >>> liste_2(2)
    8
    >>> liste_2(-5)
    2
    """
    zahlen = [2, 4, 8, 10, 12]
    print(zahlen[index])


if __name__ == "__main__":
    doctest.testmod()
