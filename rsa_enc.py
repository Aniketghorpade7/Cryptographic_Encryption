import random
from math import gcd

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def get_random_prime():
    primes = [11, 13, 17, 19, 23, 29]
    return random.choice(primes)

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def generate_keys_from_primes(p, q):
    p, q = int(p), int(q)
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p and q must be valid prime numbers.")
    if p == q:
        raise ValueError("p and q must be strictly different primes.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n), p, q, phi

def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def rsa_verify(ciphertext_blocks, guess_d, correct_d, public_key, original_text):
    try:
        guess_d = int(guess_d)
        if guess_d != correct_d:
            return False
            
        e, n = public_key
        decrypted_chars = [chr(pow(block, guess_d, n)) for block in ciphertext_blocks]
        decrypted_text = "".join(decrypted_chars)
        return decrypted_text == original_text
    except Exception:
        return False

