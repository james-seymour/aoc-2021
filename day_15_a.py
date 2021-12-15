from utils import read_aoc_input, neighbours, int_lines_to_grid
from dataclasses import dataclass
from heapq import heappush, heappop
data = read_aoc_input(15)

grid = int_lines_to_grid(data)

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


