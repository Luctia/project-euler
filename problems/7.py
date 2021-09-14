def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def nth_prime(number):
    checking = 2
    iteration = 1
    while True:
        if is_prime(checking):
            if number == iteration:
                return checking
            iteration += 1
        checking += 1


print(nth_prime(10001))
