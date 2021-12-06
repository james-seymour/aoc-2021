from utils import *


data = read_aoc_input(6)


initial = list(map(int, data[0].split(",")))

def run_day(fishes):
    for f_i, f in enumerate(fishes):
        fishes[f_i] -= 1

        if fishes[f_i] == -1:
            initial.append(9)
            fishes[f_i] = 6

    return fishes

lens = []
day = initial
for i in range(110):
    day = run_day(day)
    lens.append(len(day))







