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
        if question.isalpha() and question.isupper():
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
    Input Funktion die nur ganzezahlen erlaubt, die größer/gleich als upper_limit sind
    :param upper_limit: Minimum
    :param question: Text für den input
    :return: User Input
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            answer = int(answer)
            if answer >= upper_limit:
                return answer


def read_int_below_upper_limit(lower_limit: int,question: str) -> int:
    """
    Input Funktion die nur ganzezahlen erlaubt, die kleiner/gleich als upper_limit sind
    :param lower_limit: Maximum
    :param question: Text für den input
    :return:
    """
    while True:
        answer = input(question)
        if answer.isdecimal():
            answer = int(answer)
            if answer <= lower_limit:
                return answer
