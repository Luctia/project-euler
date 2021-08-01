def multiples(roots, limit=1000):
    res = []
    for i in range(1, limit):
        multiple = False
        for root in roots:
            if i % root == 0:
                multiple = True
        if multiple:
            res.append(i)
    return res


print(sum(multiples([3, 5])))
