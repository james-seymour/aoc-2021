from utils import *



data = read_aoc_input(5)

grid = {}

for line in data:
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))
    dx = x2 - x1
    dy = y2 - y1
    if dx: dx = dx // abs(dx)
    if dy: dy = dy // abs(dy)
    x = x1
    y = y1
    while True:
        grid[(x, y)] = grid.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

t = 0
for v in grid.values():
    if v > 1:
        t += 1

print(t)



# grid = {}
# data = [line.split("->")for line in read_aoc_input(5)]
# iterators = []
# for r in data:
#     start, end = r
#     x1, y1 = [int(s) for s in start.split(",")]
#     x2, y2 = [int(s) for s in end.split(",")]
#     x1, x2 = min(x1, x2), max(x1, x2)
#     y1, y2 = min(y1, y2), max(y1, y2)
#     for x, y in list(zip(range(x1, x2 +1), range(y1, y2 + 1))):
#         grid[(x, y)] = grid.get((x, y), 0) + 1

# t = 0
# for v in grid.values():
#     if v > 1:
#         t += 1

# print(t)

        

