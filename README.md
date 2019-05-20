# MHcrack
Взлом ранцевой криптосистема Меркля-Хеллмана с помощью LLL-метода

## Files

### testing
Основной тестирующий модуль

### mh_key_generation
Реализация этапа генерации ключей
```python
key_generation(public_key_file_path, private_key_file_path)
```

### mh_encryption
Реализация этапа шифрования
```python
mh_encrypt(public_key_file_path, plainttext_file_path, ciphertext_file_path)
```

### mh_decryption
Реализация этапа расшифрования
```python
mh_decrypt(private_key_file_path, ciphertext_file_path, plaintext_file_path)
```

### mh_constants
Константы, общие для системы:\
- `BLOCK_SIZE` - количество символов в блоке
- `BYTE_LENGTH` - костыль во избежание магических чисел
- `KEY_LENGTH` - длина открытого ключа

### utils
Необходимые реализации сторонних алгоритмов:\
```python
gcd(a, b)
extended_gcd(a, b)
mult_inverse(b, n)
gen_mutual_prime(x)
```

### crack & lll_reduction
Реализация взлома LLL-методом
