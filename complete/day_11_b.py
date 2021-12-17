from utils import read_aoc_input, int_lines_to_grid, neighbours, deep_map, count_freq, zeros

grid = int_lines_to_grid(read_aoc_input(11))

f_count = zeros(10, 10)

def step(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                flash(r, c, grid)

    return deep_map(lambda x: 0 if x > 9 else x, grid)

def flash(row, col, grid):
    f_count[row][col] += 1
    for n_r, n_c in neighbours((row, col), grid=grid, extended=True):
        grid[n_r][n_c] += 1
        if grid[n_r][n_c] == 10:
            flash(n_r, n_c, grid)

t = 0

while True:
    t += 1
    grid = step(grid)
    if count_freq(grid, flatten=True).get(0,0) == 100:
        print(t)
        break

    f_count = zeros(10, 10)