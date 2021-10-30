def primes_under(ceil):
    res = []
    for i in range(2, ceil + 1):
        is_prime = True
        for j in res:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res


# Refined
def eratosthenes(ceil):
    primes = [True for i in range(ceil + 1)]
    primes[0] = False
    primes[1] = False
    p = 2
    while p**2 <= ceil:
        if primes[p] is True:
            for i in range(p**2, ceil + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(ceil + 1) if primes[i] is True]


print(sum(primes_under(10000)))
print(sum(eratosthenes(2000000)))
