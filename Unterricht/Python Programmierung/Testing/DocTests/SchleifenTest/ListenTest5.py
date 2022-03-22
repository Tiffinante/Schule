import doctest


def listen_5(row_index, column_index):
    """
    >>> listen_5(1, 1)
    5
    >>> listen_5(1, 0)
    4
    >>> listen_5(0, 1)
    8
    >>> listen_5(-1, -1)
    1
    >>> listen_5(2, 2)
    1
    >>> listen_5(2,-1)
    1
    """
    matrix = [[7, 8, 9],
              [4, 5, 6],
              [3, 2, 1]]

    print(matrix[row_index][column_index])


if __name__ == "__main__":
    doctest.testmod()
