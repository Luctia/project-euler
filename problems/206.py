import math
import re
import time


def bruteforce_a():
    for a in range(0, 10):
        for b in range(0, 10):
            print(str(a) + str(b) + '%')
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        for f in range(0, 10):
                            for g in range(0, 10):
                                for h in range(0, 10):
                                    for i in range(0, 10):
                                        number = int(
                                            '1' + str(a) + '2' + str(b) + '3' + str(c) + '4' + str(d) + '5' + str(e) + '6' + str(f) + '7' + str(g) + '8' + str(h) + '9' + str(i) + '0'
                                        )
                                        root = math.sqrt(number)
                                        if root.is_integer():
                                            if root**2 == number:
                                                return root


def bruteforce_b():
    i = math.floor(math.sqrt(1020304050607080900))
    while True:
        if re.match(r"1\d2\d3\d4\d5\d6\d7\d8\d9\d0", str(i**2)):
            return i
        i += 1


# start = time.time()
# print(bruteforce_a())
# end = time.time()
# print(end - start)
# time: 1645s (yields no answer)
start = time.time()
print(bruteforce_b())
end = time.time()
print(end - start)
# time: 270s
