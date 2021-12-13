from utils import read_aoc_input

ds = read_aoc_input(13)[:902]
dots = set()

for line in ds:
    x, y = map(int, line.split(","))
    dots.add((x, y))

folds = read_aoc_input(13)[903:]
folds = [(fold[11:].split("=")) for fold in folds]

for t, fold in folds:
    fold = int(fold)
    if t == "x":
        dots = { (x if x < fold else fold - (x - fold), y) for x, y in dots }
    else:
        dots = { (x, y if y < fold else fold - (y - fold)) for x, y in dots }

max_r, max_c = max(y for x, y in dots) + 1, max(x for x, y in dots) + 1
grid = [["  " for _ in range(max_c)] for _ in range(max_r)]
for x, y in dots:
    grid[y][x] = "@@"
for row in grid:
    print("".join(row))