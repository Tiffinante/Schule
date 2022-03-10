def read_string(question: str) -> str:
    """
    Input Funktion die nur Große- und Kleinebuchstaben erlaubt
    :param question: Text für den Input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isalpha():
            return answer


def read_upper_case_string(question: str) -> str:
    """
    Input Funktion die nur Großebuchstaben erlaubt
    :param question: Text für den Input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isalpha() and answer.isupper():
            return answer


def read_lower_case_string(question: str) -> str:
    """
    Input Funktion die nur Kleinebuchstaben erlaubt
    :param question: Text für den Input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isalpha() and answer.islower():
            return answer


def read_int(question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt
    :param question: Text für den Input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            return int(answer)


def read_int_above_lower_limit(upper_limit: int, question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt, die größer als upper_limit sind
    :param upper_limit: Minimum
    :param question: Text für den input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            answer = int(answer)
            if answer > upper_limit:
                return answer


def read_int_below_upper_limit(lower_limit: int, question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt, die kleiner als upper_limit sind
    :param lower_limit: Maximum
    :param question: Text für den input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            answer = int(answer)
            if answer < lower_limit:
                return answer


def read_int_in_limits(lower_limit: int, upper_limit: int, question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt, die zwischen upper_limit und lower_limit liegen
    :param lower_limit: Maximum
    :param upper_limit: Minimum
    :param question: Text für den input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            answer = int(answer)
            if upper_limit > answer > lower_limit:
                return answer


def choose_option(options: list, question: str):
    """
    Input Funktion die nur Input erlaubt,  welche in einer Liste/Tupel enthalten sind, z.B. [‘a’, ’b’, ’c’]
    :param options: Liste/Tupel mit Optionen
    :param question: Text für den input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer in options:
            return answer
        elif answer.isdecimal():
            answer = int(answer)
            if answer in options:
                return answer
        elif answer == "True":
            if True in options:
                return True
        elif answer == "False":
            if False in options:
                return False
        else:
            try:
                answer = float(answer)
                return answer
            finally:
                pass


# read_string("read_string")
# read_upper_case_string("read_upper_case_string")
# read_lower_case_string("read_lower_case_string")
# read_int("read_int")
# read_int_above_lower_limit(10, "read_int_above_lower_limit")
# read_int_below_upper_limit(10, "read_int_below_upper_limit")
# read_int_in_limits(10, 20, "read_int_in_limits")
x = [2, True, "3", 4.7]
y = choose_option(x, "choose_option")
print(y)
print(type(y))
