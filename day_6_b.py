from utils import *
from collections import defaultdict
from functools import reduce
data = read_aoc_input(6)

initial = list(map(int, data[0].split(",")))


stored = defaultdict(int)
for num in initial:
    stored[num] += 1

def run_day(fishes):
    next = defaultdict(int)
    for timer in fishes.keys():
        next[timer - 1] = fishes[timer]

    new_fish = next[-1]


    next[6] += new_fish
    del next[-1]
    next[8] += new_fish
    return next


day = stored
for i in range(256):
    new_day = run_day(day)
    day = new_day

print(sum(day.values()))
