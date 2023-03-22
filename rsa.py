import random

def is_prime(num):
    """
    Check if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_keypair(p, q):
    """
    Generate public and private keys for RSA encryption
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    # Use extended Euclidean algorithm to compute the unique d such that ed ≡ 1 (mod phi(n))
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """
    Encrypt a message using RSA encryption
    """
    e, n = pk
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """
    Decrypt a message using RSA encryption
    """
    d, n = pk
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    # Generate public and private keys
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)

    # Encrypt and decrypt a message
    message = "Hello, World!"
    encrypted_message = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, encrypted_message)

    print("Original message: ", message)
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)
