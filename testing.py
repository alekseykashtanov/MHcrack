from mh_encryption import mh_encrypt
from mh_decryption import mh_decrypt
from mh_key_generation import key_generation

public_key_file = "public_key.txt"
private_key_file = "private_key.txt"
plain_in = "input_data/plaintext.txt"
cipher_in = "input_data/ciphertext.txt"
plain_out = "output_data/plaintext.txt"
cipher_out = "output_data/ciphertext.txt"

mode = input()
while mode != 'e' or mode != 'd' or mode != 'g':
    print('Usage:')
    print('g - key_generation')
    print('e - encryption')
    print('d - decryption')
    mode = input()

if mode == 'g':
    key_generation(public_key_file, private_key_file)
elif mode == 'e':
    mh_encrypt(public_key_file, plain_in, cipher_out)
elif mode == 'd':
    mh_decrypt(private_key_file, cipher_in, plain_out)
else:
    print('Wrong mode')
