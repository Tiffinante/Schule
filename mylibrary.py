# Different Color Codes
import doctest


class ColorCodes:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    TURQUOISE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'  # WHITE
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_prime(n: int) -> bool:
    """
    >>> is_prime(7)
    True
    Checks if a number is prime or not and returns True or False
    :param n: n is the number to check
    :return: True or False
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    doctest.testmod()
