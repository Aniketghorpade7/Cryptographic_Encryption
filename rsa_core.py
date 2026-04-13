# import random
# from math import gcd

# def generate_prime():
#     primes = [11, 13, 17, 19, 23, 29]
#     return random.choice(primes)

# def mod_inverse(e, phi):
#     for d in range(1, phi):
#         if (e * d) % phi == 1:
#             return d

# def generate_keys():
#     p = generate_prime()
#     q = generate_prime()

#     while p == q:
#         q = generate_prime()

#     n = p * q
#     phi = (p - 1) * (q - 1)

#     e = 3
#     while gcd(e, phi) != 1:
#         e += 2

#     d = mod_inverse(e, phi)

#     return (e, n), (d, n), p, q, phi

# def encrypt(message, public_key):
#     e, n = public_key
#     return [pow(ord(char), e, n) for char in message]

# def decrypt(cipher, private_key):
#     d, n = private_key
#     return ''.join([chr(pow(char, d, n)) for char in cipher])









import random
from math import gcd

# --- LEVEL 1: CAESAR CIPHER (EASY) ---
# Formula: C = (P + k) mod 26
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# --- LEVEL 2: BLOCK XOR (MEDIUM) ---
# Formula: C = P ⊕ K
def block_xor_encrypt(text, key=123):
    return [ord(char) ^ key for char in text]

# --- LEVEL 3: RSA (HARD) ---
# Formula: C = M^e mod n
def generate_prime():
    primes = [11, 13, 17, 19, 23, 29]
    return random.choice(primes)

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def generate_keys():
    p, q = generate_prime(), generate_prime()
    while p == q: q = generate_prime()
    n = p * q #
    phi = (p - 1) * (q - 1) #
    e = 3
    while gcd(e, phi) != 1: e += 2
    d = mod_inverse(e, phi)
    return (e, n), (d, n), p, q, phi

def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]