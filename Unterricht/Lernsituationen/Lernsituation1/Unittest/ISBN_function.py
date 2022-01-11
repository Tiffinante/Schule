def generate_check_digit(isbn_9):

    x = 1
    y = 100000000
    check_digit = 0
    while x < 10:
        check_digit += x * ((isbn_9 // y) % 10)
        x += 1
        y //= 10
    check_digit %= 11

    return check_digit


def check_ISBN(ISBN_10):
    ISBN_9 = ISBN_10 // 10
    check_digit = ISBN_10 % 10
    if generate_check_digit(ISBN_9) == check_digit:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
