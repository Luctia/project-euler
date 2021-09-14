# Bruteforce is fast enough for this problem.
sumsquare = sum([x**2 for x in range(1, 101)])
squaresum = sum(range(1, 101))**2
print(squaresum - sumsquare)
