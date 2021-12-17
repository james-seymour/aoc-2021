from utils import *



data = read_aoc_input(9)

# data = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".split("\n")
data = [[int(char) for char in line] for line in data ]


t = 0
basins = []
for r_i, r in enumerate(data):
    for c_i, c in enumerate(r):
        ns = []

        for n_r, n_c in neighbours((r_i, c_i), grid=data):
            ns.append(data[n_r][n_c])

        if False not in [ c < n for n in ns ]:
            basins.append((r_i, c_i))

ts = []
for basin in basins:
    frontier = [basin]
    visited = set()
    t = 0
    while frontier:
        b_r, b_c = frontier.pop(-1)
        if (b_r, b_c) in visited:
            continue

        t += 1
        visited.add((b_r, b_c))

        for n_r, n_c in neighbours((b_r, b_c),grid=data):
            if int(data[n_r][n_c]) < 9:
                frontier.append((n_r, n_c))

    ts.append(t)

ts.sort(reverse=True)
print(prod(ts[:3]))