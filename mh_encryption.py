from mh_types import BLOCK_SIZE


def mh_encrypt(key_file_path, plainttext_file_path, ciphertext_file_path):
    keys_input = open(key_file_path, 'r')
    plaintext_input = open(plainttext_file_path, 'r')
    ciphertext_file = open(ciphertext_file_path, 'w')

    public_key = [line.strip() for line in keys_input]
    plaintext = bytearray(plaintext_input.read())

    

