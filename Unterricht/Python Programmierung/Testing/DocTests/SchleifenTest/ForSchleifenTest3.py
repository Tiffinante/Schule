import doctest


def for_schleife_summieren(end):
    """
    >>> for_schleife_summieren(4)
    0
    1
    3
    6
    >>> for_schleife_summieren(5)
    0
    1
    3
    6
    10
    >>> for_schleife_summieren(2)
    0
    1
    """
    summe = 0
    for i in range(end):
        summe += i
        print(summe)


if __name__ == "__main__":
    doctest.testmod()
