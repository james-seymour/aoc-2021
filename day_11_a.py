from utils.data import read_aoc_input
from utils.grid import neighbours
from utils.builtins import deepmap

grid = [[int(char) for char in line] for line in read_aoc_input(11) ]

t = 0

def step(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                flash(r, c, grid)

    return deepmap(lambda x: 0 if x > 9 else x, grid)

def flash(row, col, grid):
    global t
    t += 1
    for n_r, n_c in neighbours((row, col), grid=grid):
        grid[n_r][n_c] += 1
        if grid[n_r][n_c] == 10:
            flash(n_r, n_c, grid)

for _ in range(100):
    grid = step(grid)

print(t)




    





# step(grid)
# step(grid)