import doctest


def for_schleife_2(end):
    """
    >>> for_schleife_2(13)
    12
    >>> for_schleife_2(8)
    7
    """
    wert = 0
    for i in range(end):
        wert = i
    print(wert)


if __name__ == "__main__":
    doctest.testmod()
