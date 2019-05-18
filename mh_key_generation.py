# @brief Merkle-Hellman cryptosystem key generation function

from mh_types import BLOCK_SIZE
from utils import gen_mutual_prime
import random


def key_generation(public_key_file_path, private_key_file_path):
    public_key = []
    private_key = []
    s = 0
    random.seed()

    # Генерация супервозрастающей последовательности')
    for i in range(BLOCK_SIZE - 1):
        w = random.randint(s, s << 1)
        s += w
        private_key[i] = w

    # Генерация q > sum(w_i)
    q = random.randint(s + 1, s << 1)
    print("q: ", q)

    # Генерация r, взаимнопростого с q
    r = gen_mutual_prime(q)
    print('r: ', r)

    private_key.append(q)
    private_key.append(r)

    # Генерация открытого ключа
    for i in range(BLOCK_SIZE - 1):
        public_key.append(public_key[i]*r % q)

    # Запись ключей в файл
    try:
        pub_k = open(public_key_file_path, 'w')
        priv_k = open(private_key_file_path, 'w')
        for elem in public_key:
            pub_k.write(elem + '\n')
        for elem in private_key:
            priv_k.write(elem + '\n')
    except IOError:
        print("key_generation: IOError")
    finally:
        pub_k.close()
        priv_k.close()

    return
