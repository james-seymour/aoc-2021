from utils import read_aoc_input, int_lines_to_grid, neighbours, deep_map, zeros
from dataclasses import dataclass
from heapq import heappush, heappop

data = read_aoc_input(15)

grid = int_lines_to_grid(data)
row_l = len(grid)
col_l = len(grid[0])

extended_grid = zeros(5 * row_l, 5 * col_l)

def get_nth_grid(grid, n):
    if n == 0: return grid
    new = deep_map(lambda x: x % 9 + 1, grid)
    return get_nth_grid(new, n - 1)

# Place new grids in extended grid
for i in range(5):
    for j in range(5):
        new = get_nth_grid(grid, i + j)
        for row_i in range(len(new)):
            for col_i in range(len(new[row_i])):
                extended_grid[i * row_l + row_i][j * col_l + col_i] = new[row_i][col_i]

grid = extended_grid

@dataclass
class Node:
    x: int
    y: int
    risk_level: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return self.risk_level < other.risk_level


visited = set()
frontier = [Node(0, 0, 0)]
def search():
    while frontier:
        current = heappop(frontier)

        if current.y == len(grid) - 1 and current.x == len(grid[0]) - 1:
            return current

        if hash(current) in visited:
            continue

        visited.add(hash(current))

        valid_children = [Node(c, r, current.risk_level + grid[r][c]) for r, c in neighbours((current.y, current.x), grid=grid)]
        for child in valid_children:
            heappush(frontier, child)

print(search())








        



