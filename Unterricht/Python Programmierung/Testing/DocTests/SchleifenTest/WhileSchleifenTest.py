import doctest


def while_schleife_1():
    """
    >>> while_schleife_1()
    10
    """
    wert = 1
    while wert < 10:
        wert = wert + 1
    return wert


if __name__ == "__main__":
    doctest.testmod()
