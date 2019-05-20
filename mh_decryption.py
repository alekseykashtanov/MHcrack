from mh_constants import *
from utils import mult_inverse


def mh_decrypt(private_key_file_path, ciphertext_file_path, plaintext_file_path):
    try:
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
            counter = 0  # Счетчик для выделения отдельных байтов
            # Жадный алгоритм
            for ww in w:
                counter += 1
                plain_byte <<= 1
                if tmp >= ww:
                    plain_byte += 1
                    tmp -= ww
                if counter == BYTE_LENGTH:
                    plaintext_file.write(chr(plain_byte))
                    counter = plain_byte = 0

    except IOError:
        print('mh_decryption: IOError')

    else:
        print('Successful decryption')

        key_input.close()
        ciphertext_file.close()
        plaintext_file.close()
        return
