def palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False


def largest_palindrome():
    largest = 1
    smallest_multiple = 1
    for i in range(999, smallest_multiple, -1):
        for j in range(999, smallest_multiple, -1):
            if palindrome(i * j) and i * j > largest:
                largest = i * j
                smallest_multiple = min(i, j)
                break
    return largest


print(largest_palindrome())
