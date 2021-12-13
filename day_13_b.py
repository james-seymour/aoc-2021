from utils import read_aoc_input, full, flatten

dots = read_aoc_input(13)[:902]
folds = read_aoc_input(13)[903:]

folds = [(fold[11:].split("=")) for fold in folds]
dots = [(int(line.split(",")[1]), int(line.split(",")[0])) for line in dots]

max_row = max(*[d[0] for d in dots])
max_col = max(*[d[1] for d in dots])

def get_col_iter(fold_along, max_col):
    return zip(range(0, fold_along), range(max_col, fold_along, -1))

def get_row_iter(fold_along, max_row):
    return zip(range(0, fold_along), range(max_row, fold_along, -1))

grid = full(max_row + 1, max_col + 1, ".")
for r, c in dots:
    grid[r][c] = "#"

def reflect(grid, axis, num):
    if axis == "x":
        for row_i, row in enumerate(grid):
            for s_c, e_c in get_col_iter(num, num*2):
                if grid[row_i][e_c] == "#":
                    grid[row_i][s_c] = "#"
                    grid[row_i][e_c] = "."

    if axis == "y":
        for col_i, col in enumerate(zip(*grid)):
            for s_r, e_r in get_row_iter(num, num*2):
                if grid[e_r][col_i] == "#":
                    grid[s_r][col_i] = "#"
                    grid[e_r][col_i] = "."

    return grid

for axis, line in folds:
    grid = reflect(grid, axis, int(line))

for row in grid[:6]:
    print("".join(row[:39]).replace(".", " ").replace("#","@"))