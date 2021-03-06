# @brief Merkle-Hellman cryptosystem key generation function

from mh_constants import *
from utils import gen_mutual_prime
import random


def key_generation(public_key_file_path, private_key_file_path):
    public_key = []
    private_key = []
    s = 10
    random.seed()

    # Генерация супервозрастающей последовательности
    for i in range(KEY_LENGTH):
        w = random.randint(s, s << 1)
        s += w
        private_key.append(w)

    # Генерация q > sum(w_i)
    q = random.randint(s + 1, s << 1)

    # Генерация r, взаимнопростого с q
    r = gen_mutual_prime(q)

    private_key.append(q)
    private_key.append(r)

    # Генерация открытого ключа
    for i in range(KEY_LENGTH):
        public_key.append(r*private_key[i] % q)

    # Запись ключей в файл
    try:
        pub_k = open(public_key_file_path, 'w')
        priv_k = open(private_key_file_path, 'w')
        for elem in public_key:
            pub_k.write(str(elem) + '\n')
        for elem in private_key:
            priv_k.write(str(elem) + '\n')
    except IOError:
        print("key_generation: IOError")
    else:
        print('Successful generation of keys')
        pub_k.close()
        priv_k.close()

    return
