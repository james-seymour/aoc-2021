from utils.data import read_aoc_input
from utils.grid import neighbours

data = read_aoc_input(9)
# data = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".split("\n")

data = [[int(char) for char in line] for line in data ]



t = 0
for r_i, r in enumerate(data):
    for c_i, c in enumerate(r):
        ns = []

        for n_r, n_c in neighbours((r_i, c_i),grid=data):
            ns.append(data[n_r][n_c])

        if False not in [ c < n for n in ns ]:
            t += c + 1


print(t) 





