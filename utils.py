# @brief Utils for MHCS

from random import randint


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def gen_mutual_prime(x):
    tmp = randint(0, x << 4)
    while gcd(tmp, x) > 1:
        tmp = randint(0, x << 4)
    return tmp


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x


def mult_inverse(b, n):
    g, x, _ = extended_gcd(b, n)
    if g == 1:
        return x % n
