with open('resources/11grid.txt') as lines:
    grid = []
    for line in lines.readlines():
        grid.append([int(x) for x in line[:-1].split(' ')])
    highest = 0
    # Right
    for i in range(16):
        for j in range(20):
            product = grid[j][i] * grid[j][i + 1] * grid[j][i + 2] * grid[j][i + 3]
            highest = product if product > highest else highest
    # Down
    for i in range(20):
        for j in range(16):
            product = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            highest = product if product > highest else highest
    # Diagonal DR
    for i in range(16):
        for j in range(16):
            product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            highest = product if product > highest else highest
    # Diagonal DL
    for i in range(16):
        for j in range(3, 20):
            product = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
            highest = product if product > highest else highest
    print(highest)
