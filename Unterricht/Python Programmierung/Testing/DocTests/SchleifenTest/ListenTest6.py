import doctest


def listen_5(row_index, column_index):
    """
    >>> listen_5(5,2)
    13
    >>> listen_5(2,0)
    5
    >>> listen_5(1,3)
    2
    >>> listen_5(-3,0)
    5
    """
    matrix = []
    value = 0
    for x in range(1, 6):
        row = []
        for y in range(1, 4):
            row.append(value)
            value += 1
        matrix.append(row)

    print(matrix[row_index-1][column_index-1])


if __name__ == "__main__":
    doctest.testmod()
