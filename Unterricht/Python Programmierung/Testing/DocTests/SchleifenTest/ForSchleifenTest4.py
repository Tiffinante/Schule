import doctest


def for_schleife_summieren(start, end, step):
    """
    >>> for_schleife_summieren(2,5,1)
    2
    3
    4
    >>> for_schleife_summieren(2,7,2)
    2
    4
    6
    >>> for_schleife_summieren(2,8,2)
    2
    4
    6
    >>> for_schleife_summieren(10,0,-2)
    10
    8
    6
    4
    2
    >>> for_schleife_summieren(10, 8, -2)
    10
    """
    for i in range(start, end, step):
        print(i)


if __name__ == "__main__":
    doctest.testmod()
