from mh_types import BLOCK_SIZE
from utils import mult_inverse


def mh_decrypt(private_key_file_path, ciphertext_file_path, plaintext_file_path):
    key_input = open(private_key_file_path, 'r')
    ciphertext_file = open(ciphertext_file_path, 'r')
    plaintext_file = open(plaintext_file_path, 'w')

    private_key = [int(line.strip()) for line in key_input]
    ciphertext = [int(line.strip()) for line in ciphertext_file]

    q = private_key[-2]
    w = private_key[:-2]
    w.reverse()
    r_inv = mult_inverse(private_key[-1], q)

    for cipher_elem in ciphertext:
        tmp = cipher_elem * r_inv % q
        plain_byte = 0
        # Жадный алгоритм
        for i in range(BLOCK_SIZE):
            plain_byte <<= 1
            if tmp >= w[i]:
                plain_byte += 1
                tmp -= w[i]
        plaintext_file.write(chr(plain_byte))

    key_input.close()
    ciphertext_file.close()
    plaintext_file.close()
    return
