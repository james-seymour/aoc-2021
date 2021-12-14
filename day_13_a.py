from utils import read_aoc_input

data = read_aoc_input(13)[:902]
dots = set()

for line in data:
    x, y = map(int, line.split(","))
    dots.add((x, y))

dots = { (x if x < 655 else 655 - (x - 655), y) for x, y in dots }
print(len(dots))
