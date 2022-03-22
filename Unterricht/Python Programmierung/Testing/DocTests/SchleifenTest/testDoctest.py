import doctest


def values_between(min, max):
    """
    >>> values_between(3, 8)
    4
    5
    6
    7
    >>> values_between(-2, 2)
    -1
    0
    1
    """
    for i in range(min+1, max):
        print(i)


if __name__ == "__main__":
    doctest.testmod()

