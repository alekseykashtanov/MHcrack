# @brief Utils for MHCS

import random


def gcd (a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def gen_mutual_prime(x):
    tmp = random.randint()
    while gcd(tmp, x) > 1:
        tmp = random.randint()
    return tmp
