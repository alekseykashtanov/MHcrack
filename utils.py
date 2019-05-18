# @brief Utils for MHCS

import random


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def gen_mutual_prime(x):
    tmp = random.randint()
    while gcd(tmp, x) > 1:
        tmp = random.randint()
    return tmp


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mult_inverse(b, n):
    g, x, _ = extended_gcd(b, n)
    if g == 1:
        return x % n
