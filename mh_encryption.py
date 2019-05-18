from mh_types import BLOCK_SIZE


def mh_encrypt(public_key_file_path, plainttext_file_path, ciphertext_file_path):
    key_input = open(public_key_file_path, 'r')
    plaintext_input = open(plainttext_file_path, 'r')
    ciphertext_file = open(ciphertext_file_path, 'w')

    public_key = [int(line.strip()) for line in key_input]
    plaintext = bytearray(plaintext_input.read())

    for elem in plaintext:
        s = 0
        for i in range(BLOCK_SIZE - 1):
            s += elem[i] * public_key[i]
        ciphertext_file.write(str(s) + ' ')

    key_input.close()
    plaintext_input.close()
    ciphertext_file.close()
