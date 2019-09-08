# @brief LLL_reduction algorithm
from utils import scalar_product


def gram_schmidt(basis):
    rbs = []
    mus = []

    for b in basis:
        tmp_rb = b[:]
        tmp_mu = []

        for r in rbs:
            coef = scalar_product(r, tmp_rb) / scalar_product(r, r)
            for k, r_k in enumerate(r):
                tmp_rb[k] -= coef * r_k
            tmp_mu.append(coef)

        rbs.append(tmp_rb)
        mus.append(tmp_mu)

    return rbs, mus


def find_bad_i(b, mus, delta):
    for i in range(0, len(b) - 1):
        lhs = delta * scalar_product(b[i], b[i])
        rhs = scalar_product(b[i], b[i]) * (mus[i+1][i] ** 2) + scalar_product(b[i+1], b[i+1])
        if lhs > rhs:
            return i
    return None


def delta_lll_reduce(basis, mus):
    for i in range(1, len(basis)):      # перебираем векторы базиса без первого
        for j in range(i - 1, -1, -1):  # вычетаем уже обработанные в обратном порядке
            c = round(mus[i][j])
            for k, b_k in enumerate(basis[j]):
                basis[i][k] -= c * b_k

            mus[i][j] -= c
            for k in range(j):
                mus[i][k] -= c * mus[j][k]


def delta_lll_swap(lll_b, gsh_b, mus, delta):
    idx = find_bad_i(gsh_b, mus, delta)
    if idx is None:
        return True

    lll_b[idx], lll_b[idx + 1] = lll_b[idx + 1], lll_b[idx]
    return False


def delta_lll(basis, delta):
    alright = False
    lll_b = [b[:] for b in basis]

    while not alright:
        gsh_b, mus = gram_schmidt(lll_b)
        delta_lll_reduce(lll_b, mus)
        alright = delta_lll_swap(lll_b, gsh_b, mus, delta)

    return lll_b
