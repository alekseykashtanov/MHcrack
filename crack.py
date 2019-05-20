from lll_reduction import delta_lll


def cracking(ciphertext_file_path, public_key_file_path):
    key_input = open(public_key_file_path, 'r')
    public_key = [int(line.strip()) for line in key_input]
    ciphertext = [int(line.strip()) for line in open(ciphertext_file_path, 'r')]

    delta = 0.75

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
        probable_answer = delta_lll(basis, delta)[0]

        probable_answer.reverse()
        print(probable_answer)
        c = 0
        for i in range(len(probable_answer) - 1):
            c += probable_answer[i]
            c <<= 1
        print('Symbol: ', chr(c))
    return
