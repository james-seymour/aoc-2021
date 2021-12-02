from utils import *


data = parse_int_to_list(read_aoc_input(1))

# Part 1
increases = 0
for depth, next_depth in zip(data, data[1:]):
    if next_depth > depth:
        increases += 1


# Part 2
sliding_window = []
for first_depth, second_depth, third_depth in zip(data, data[1:], data[2:]):
    sliding_window.append(first_depth + second_depth + third_depth)

increases = 0
for depth, next_depth in zip(sliding_window, sliding_window[1:]):
    if next_depth > depth:
        increases += 1

print(increases)