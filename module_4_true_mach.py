# module_4_true_mach
from math import inf


def divide(first, second):
    # Можно отработать исключение, но так будет проще
    if second == 0:
        return inf
    else:
        return first / second
