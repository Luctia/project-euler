def fibonacci(a=1, b=2):
    total = 0
    if b % 2 == 0:
        total += b
    if a + b < 4000000:
        total += fibonacci(b, a + b)
    return total


print(fibonacci())
