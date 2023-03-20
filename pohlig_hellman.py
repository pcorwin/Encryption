from math import gcd

def pohlig_hellman(g, h, p, factors):
    """
    Solves the discrete logarithm problem g^x = h (mod p) using the Pohlig-Hellman algorithm.
    Assumes that the order of g is p-1 and that the prime factors of p-1 are known.
    """
    x = 0
    for prime, k in factors.items():
        # Compute g_i = g^(n/p_i^k)
        g_i = pow(g, (p-1)//(prime**k), p)
        # Compute h_i = h^(n/p_i^k)
        h_i = pow(h, (p-1)//(prime**k), p)
        # Compute y_i using the naive algorithm for discrete logarithms in prime-power groups
        y_i = 0
        for j in range(k):
            y_i += ((h_i * pow(g_i, y_i*(prime**(k-j-1)), p) % p)* pow(g_i, j*(prime**(k-j-1)), p)) % p
        # Solve for x_i using the Chinese Remainder Theorem
        x_i = (y_i * pow((p-1)//prime**k, -1, prime**k)) % (p-1)
        # Combine with other factors
        x += x_i * (p-1)//prime**k * pow(prime, k-1)
    return x

# Example usage:
g = 2
h = 8
p = 11
factors = {11: 1, 5: 1}
x = pohlig_hellman(g, h, p, factors)
print(f'x = {x}')