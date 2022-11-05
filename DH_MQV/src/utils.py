def sieve_of_eratosthenes(n=10000):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    primes = []
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes


def find_prime_roots(modulo):
    res = []
    for g in range(1, modulo):
        modulos = set(g ** i %
                      modulo for i in range(1, modulo))
        if modulos == set(range(1, modulo)):
            res.append(g)
    return res
