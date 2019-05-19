from mh_types import BLOCK_SIZE


def mh_encrypt(public_key_file_path, plainttext_file_path, ciphertext_file_path):
    try:
        key_input = open(public_key_file_path, 'r')
        plaintext_input = open(plainttext_file_path, 'r')
        ciphertext_file = open(ciphertext_file_path, 'w')

        public_key = [int(line.strip()) for line in key_input]
        plaintext = plaintext_input.read()

        for elem in plaintext:
            s = 0
            tmp = ord(elem)
            for i in range(BLOCK_SIZE):
                s += (tmp & 1) * public_key[i]
                tmp >>= 1
            ciphertext_file.write(str(s) + '\n')

        key_input.close()
        plaintext_input.close()
        ciphertext_file.close()
    except IOError:
        print('mh_encrypt: IOError')
    finally:
        key_input.close()
        plaintext_input.close()
        ciphertext_file.close()
