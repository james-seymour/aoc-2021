from utils import *
from itertools import *

data = read_aoc_input(8)

total = 0

for line in data:
    encoding, goal = line.split(" | ")
    num_codes = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    required_set = set(num_codes)
    for x in permutations("abcdefg"):
        potential_map = {i: j for i, j in zip(x, "abcdefg")}
        potential_set = set()

        for q in encoding.split():
            sorted_possibility = sorted(map(potential_map.get, q))
            potential_set.add("".join(sorted_possibility))

        if potential_set == required_set:
            b = ["".join(sorted(map(potential_map.get, q))) for q in goal.split()]
            b = "".join(str(num_codes.index(q)) for q in b)
            total += int(b)

print(total)









