import doctest


def while_schleife_2():
    """
    >>> while_schleife_2()
    5
    6
    7
    8
    """
    wert = 4
    while True:
        if wert < 8:
            wert += 1
        else:
            break
        print(wert)


if __name__ == "__main__":
    doctest.testmod()
