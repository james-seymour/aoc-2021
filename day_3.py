from utils import *
from collections import defaultdict

data = read_aoc_input(3)
grid = [ list(number) for number in data ]
N_COLS = 12

# Part 1
def calculate_zeros_ones(grid):
    zeros = defaultdict(int)
    ones = defaultdict(int)
    for row_i, row in enumerate(grid):
        for col_i, bit in enumerate(row):
            if bit == "0":
                zeros[col_i] += 1
            if bit == "1":
                ones[col_i] += 1

    return zeros, ones

zeros, ones = calculate_zeros_ones(grid)

gamma = []
epsilon =[]
for col_i in range(N_COLS):
    if zeros[col_i] > ones[col_i]:
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma * epsilon)

# Part 2

def get_dominant_bit(zeros, ones, col_i):
    if zeros.get(col_i, 0) > ones.get(col_i, 0):
        return "0"
    return "1"

def get_smallest_bit(zeros, ones, col_i):
    if zeros.get(col_i, 0) > ones.get(col_i, 0):
        return "1"
    return "0"

def filter_grid(min_max_func):
    new_grid = data
    for col_i in range(N_COLS):
        zeros, ones = calculate_zeros_ones(new_grid)

        dominant_bit = min_max_func(zeros, ones, col_i)

        new_grid_list = []
        for number in new_grid:
            if number[col_i] == dominant_bit:
                new_grid_list.append(number)

        new_grid = new_grid_list

        if len(new_grid) == 1:
            return new_grid[0]

oxygen_bin = filter_grid(get_dominant_bit)
co2_bin = filter_grid(get_smallest_bit)

oxygen = bin_to_int(oxygen_bin)
co2 = bin_to_int(co2_bin)

print(oxygen * co2)