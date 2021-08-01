def find_factors(prime, largest_factor=1):
    if prime == 1:
        return []
    for i in range(largest_factor + 1, prime + 1):
        if prime % i == 0:
            return [i]+find_factors(prime // i, i)
    return [prime]


print(find_factors(600851475143))
