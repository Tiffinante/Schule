import doctest


def for_schleife_1():
    """
    >>> for_schleife_1()
    0
    1
    2
    3
    """

    for i in range(4):
        print(i)


if __name__ == "__main__":
    doctest.testmod()
