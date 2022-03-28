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
    Checks if a number is prime or not and returns True or False.
    :param n: is the number to check.
    :return: True if it is a prime number ans False if it is not a prime number.
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def input_integer(question: str) -> int:
    """
    Input function that only accepts integers.
    :param question: Text for the input.
    :return: User Input as integer.
    """
    while True:
        n = input(question)
        if n.isdecimal():
            return int(n)
