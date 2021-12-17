from utils import *

data = [ line.strip().split(" ") for line in read_aoc_input(2) ]

# Part 1
x_dist, depth = 0, 0
for dir, amount in data:
    x = int(amount)
    match dir:
        case "forward":
            x_dist += x
        case "down":
            depth += x
        case "up":
            depth -= x

print(x_dist * depth)

# Part 2
x_dist, depth, aim = 0, 0, 0
for dir, amount in data:
    x = int(amount)
    match dir:
        case "forward":
            x_dist += x
            depth += aim * x
        case "down":
            aim += x
        case "up":
            aim -= x

print(x_dist * depth)
