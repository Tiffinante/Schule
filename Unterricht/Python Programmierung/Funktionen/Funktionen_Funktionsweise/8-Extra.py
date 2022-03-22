def sum_of_2(x: int, y: int) -> float:
    return (x + y) / 2


def sum_of_list(l: list) -> float:
    summe = 0
    for i in l:
        summe += i
    return summe / len(l)


def sum_of_tuple(t: tuple) -> float:
    summe = 0
    for i in t:
        summe += i
    return summe / len(t)


def ggt(a: int, b: int) -> int:
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def is_prim(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
