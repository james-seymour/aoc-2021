from utils import *
from collections import defaultdict
from itertools import product

data = read_aoc_input(5)
# data = [line.split("->")for line in read_aoc_input(5)]
# iterators = []
# for r in data:
#     start, end = r
#     x1, y1 = [int(s) for s in start.split(",")]
#     x2, y2 = [int(s) for s in end.split(",")]
#     x1, x2 = min(x1, x2), max(x1, x2)
#     y1, y2 = min(y1, y2), max(y1, y2)
#     iterators.append(([_ for _ in range(x1, x2 + 1)], [_ for _ in range(y1, y2 + 1)]))

# stored = defaultdict(int)


# for iterator in iterators:
#     x_range, y_range = iterator
#     for x, y in product(x_range, y_range):
#         stored[(x,y)] += 1



# print(len(list(filter(lambda val: val >= 2, stored.values()))))
grid = {}

for line in data.splitlines():
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x, y)] = grid.get((x, y), 0) + 1

t = 0
for v in grid.values():
    if v > 1:
        t += 1

print(t)