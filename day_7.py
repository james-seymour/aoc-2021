from utils import *
from copy import deepcopy

data = list(map(int, read_aoc_input(7)[0].split(",")))

totals = []
for i, pos in enumerate(data):
    new = deepcopy(data)
    new.pop(i)
    total = 0
    for n_pos in new:
        n = abs(n_pos - pos)
        total += int(n*(n + 1)/2)

    totals.append(total)

print(min(totals))

