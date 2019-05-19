from mh_encryption import mh_encrypt
from mh_decryption import mh_decrypt
from mh_key_generation import key_generation

public_key_file = "public_key.txt"
private_key_file = "private_key.txt"

key_generation(public_key_file, private_key_file)
