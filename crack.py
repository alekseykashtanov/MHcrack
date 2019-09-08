from lll_reduction import delta_lll
from utils import b2c


def check_answer(v):
    for w in v:
        if w != 0 and w != 1:
            return False
    if v[len(v) - 1] != 0:
        return False
    return True


def cracking(ciphertext_file_path, public_key_file_path):
    try:
        key_input = open(public_key_file_path, 'r')
        public_key = [int(line.strip()) for line in key_input]
        cipher_file = open(ciphertext_file_path, 'r')
        ciphertext = [int(line.strip()) for line in cipher_file]

        delta = 0.99
        result_bin = []

        for elem in ciphertext:
            print('Trying for ', elem)

            # Подготовка базиса решетки
            basis = []
            size = len(public_key) + 1
            for i in range(size):
                basis.append([])
                for j in range(size):
                    tmp = 0
                    if j == size - 1:
                        if i == j:
                            tmp = elem
                        else:
                            tmp = -public_key[i]
                    elif i == j:
                        tmp = 1
                    basis[i].append(tmp)
            # Первый вектор полученного базиса - кандидат на решение
            probable_answer = delta_lll(basis, delta)

            # if check_answer(probable_answer[0]) is False:
            #     tmp_sum = 0
            #     for v in public_key:
            #         tmp_sum += v
            #     basis[size - 1][size - 1] = tmp_sum - elem
            #     probable_answer = delta_lll(basis, delta)

            probable_answer[0].reverse()
            print(probable_answer[0][:-1])
            result_bin.extend(probable_answer[0][:-1])
        print(b2c(result_bin))
    except IOError:
        print('crack: IOError')
    else:
        key_input.close()
        cipher_file.close()
        return
