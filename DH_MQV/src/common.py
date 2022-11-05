from random import choice
from src.utils import sieve_of_eratosthenes, find_prime_roots


# common function, same output for both parties
def choose_n_and_g(max_n=1000):
    primes = sieve_of_eratosthenes()

    n = choice(primes)
    while n > max_n:
        n = choice(primes)

    prime_roots = find_prime_roots(n)
    g = choice(prime_roots)
    return n, g
