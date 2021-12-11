from utils.data import read_aoc_input
from utils.grid import neighbours
from utils.builtins import deepmap, flatten

grid = [[int(char) for char in line] for line in read_aoc_input(11) ]

f_count = [ [0] * len(r) for r in grid ] 

def step(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                flash(r, c, grid)

    return deepmap(lambda x: 0 if x > 9 else x, grid)

def flash(row, col, grid):
    global t
    f_count[row][col] += 1
    for n_r, n_c in neighbours((row, col), grid=grid):
        grid[n_r][n_c] += 1
        if grid[n_r][n_c] == 10:
            flash(n_r, n_c, grid)

t = 0

while True:
    t += 1
    grid = step(grid)
    if all(flatten(deepmap(lambda x: x == 0, grid))):
        print(t)
        break

    f_count = [[0] * len(r) for r in grid]