from mh_constants import *


def block_encryption(block, key):
    k = 1
    s = 0

    print('#', block, '#')

    for c in block:
        tmp = bin(ord(c))[2:]
        #Дополнение до 8 бит //Костыль, потом поправить
        if len(tmp) < BYTE_LENGTH:
            for i in range(BYTE_LENGTH - len(tmp)): tmp = '0' + tmp
        for b in tmp:
            if '1' == b:
                s += key[-k]
            k += 1
    return s


def mh_encrypt(public_key_file_path, plainttext_file_path, ciphertext_file_path):
    try:
        key_input = open(public_key_file_path, 'r')
        plaintext_input = open(plainttext_file_path, 'r')
        ciphertext_file = open(ciphertext_file_path, 'w')

        public_key = [int(line.strip()) for line in key_input]
        plaintext = plaintext_input.read()
        print(plaintext)
        result = []

        for block_idx in range(len(plaintext) // BLOCK_SIZE + 1):
            block = plaintext[block_idx * BLOCK_SIZE: (block_idx + 1) * BLOCK_SIZE]
            result_ = block_encryption(block, public_key)
            result.append(result_)

        for elem in result:
            ciphertext_file.write(str(elem) + '\n')


    except IOError:
        print('mh_encrypt: IOError')

    else:
        print('Successful encryption')

        key_input.close()
        plaintext_input.close()
        ciphertext_file.close()
