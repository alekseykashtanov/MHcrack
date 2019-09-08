# @brief Utils for MHCS

from random import randint


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def gen_mutual_prime(x):
    counter = 1
    tmp = randint(0, x << 4)
    while gcd(tmp, x) > 1:
        counter += 1
        tmp = randint(0, x << 4)
    print(counter)
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

def b2c(vector):
    result = ''
    byte_counter = 0
    tmp = 0
    for elem in vector:
        byte_counter += 1
        tmp += elem
        tmp <<= 1
        if byte_counter == 8:
            result += chr(tmp)
            tmp = byte_counter = 0
    return result


def scalar_product(a, b):
    return sum([a_i * b_i for a_i, b_i in zip(a, b)])
