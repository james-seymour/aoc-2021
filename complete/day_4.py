from math import prod
from utils import * 
from copy import deepcopy

data = read_aoc_input(4)

numbers_drawn = [number for number in  map(int, data[0].split(","))]

split_indices = [ index for index, line in enumerate(data) if line == ""]


def create_grids():
    grids = []
    for index_1, index_2 in zip(split_indices, split_indices[1:]):
        grid_str = data[index_1 + 1: index_2]
        grid = [[num for num in map(int, list(filter(lambda a: a != "" and a != " ", line.split(" "))))] for line in grid_str]
        grids.append(grid)
    return grids

def check_win(grid):
        # Check rows
    for row_i, row in enumerate(grid):
        if all([elem == "X" for elem in row]):
            return True
    # Check cols
    for col_i in range(5):
        col = [row[col_i] for row in grid]
        if all([elem == "X" for elem in col]):
            return True

    return False

grids = create_grids()

def find_winning_grid():
    for num_i, num in enumerate(numbers_drawn):
        for grid_i, grid in enumerate(grids):
            for row_i, row in enumerate(grid):
                for col_i, elem in enumerate(row):
                    if elem == num:
                        grids[grid_i][row_i][col_i] = "X"

            if check_win(grids[grid_i]):
                return grid_i, num



def sum_win(win):
    return sum([num for row in win for num in row if num != "X"])
# Part 1
# print(numbers_drawn)
win, num = find_winning_grid()
# print(grids[win], num)
print(sum_win(grids[win]) * num) 




# Part 2

grids = create_grids()

def mark_number(grids, num):
    for grid_i, grid in enumerate(grids):
        for row_i, row in enumerate(grid):
            for col_i, elem in enumerate(row):
                if elem == num:
                    grids[grid_i][row_i][col_i] = "X"

    return grids

def check_all_win(grids):
    wins_bool = [ check_win(grid) for grid in grids ]
    number_of_wins = sum(wins_bool)
    if number_of_wins > len(grids) - 3:
        return True

def find_last_grid():
    grids_copy = create_grids()
    for num_i, num in enumerate(numbers_drawn):
        new_grids = mark_number(grids_copy, num)
        if check_all_win(new_grids):
            return grids_copy, num
        
        grids_copy = new_grids

grids, number = find_last_grid()
grids = mark_number(grids, 75)
grids = mark_number(grids, 87)
number = 6
for grid in grids:
    if not check_win(grid):
        print((sum_win(grid)-6) * number)














