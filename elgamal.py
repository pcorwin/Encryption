
import random
from math import gcd

def generate_keys(p):
    g = random.randint(2, p-1)
    x = random.randint(2, p-2)
    h = pow(g, x, p)
    public_key = (p, g, h)
    private_key = x
    return (public_key, private_key)

def encrypt(plaintext, public_key):
    p, g, h = public_key
    y = random.randint(1, p-2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = [(ord(m) * s) % p for m in plaintext]
    return (c1, c2)

def decrypt(ciphertext, private_key, public_key):
    c1, c2 = ciphertext
    p, g, h = public_key
    s = pow(c1, private_key, p)
    s_inv = pow(s, -1, p)
    plaintext = [chr((c * s_inv) % p) for c in c2]
    return ''.join(plaintext)

# Example usage:
plaintext = "Hello, world!"
p = 53
public_key, private_key = generate_keys(p)
ciphertext = encrypt(plaintext, public_key)
decrypted_text = decrypt(ciphertext, private_key, public_key)
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
print(f'Decrypted text: {decrypted_text}')