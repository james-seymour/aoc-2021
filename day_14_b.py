from utils import read_aoc_input
from collections import defaultdict

data = read_aoc_input(14)

base = data[0].strip()
rules = dict([line.split(" -> ") for line in data[2:]])

pair_count = defaultdict(int)
for x, y in zip(base, base[1:]):
    pair_count[x + y] += 1

for _ in range(40):
    new_pair_count = defaultdict(int)
    for pair in pair_count.keys():
        insert = rules[pair]
        first_l, second_l = pair

        new_pair_count[first_l + insert] += pair_count[pair]
        new_pair_count[insert + second_l] += pair_count[pair]

    pair_count = new_pair_count

print(pair_count)
first_count = defaultdict(int)
second_count = defaultdict(int)

for pair in pair_count.keys():
    first_l, second_l = pair
    first_count[first_l] += pair_count[pair]
    second_count[second_l] += pair_count[pair]

counts = {char: max(first_count[char], second_count[char]) for char in first_count.keys()}

print(max(counts.values()) - min(counts.values()))