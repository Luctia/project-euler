def bruteforce(target):
    for a in range(1, target + 1):
        for b in range(a, target + 1 - a):
            for c in range(b, target + 1 - a - b):
                if a**2 + b**2 == c**2 and a + b + c == target:
                    return a * b * c
    return -1


print(bruteforce(1000))
