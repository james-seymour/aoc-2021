from utils import read_aoc_input
from collections import defaultdict, Counter

data = read_aoc_input(14)

base = data[0].strip()
rules = dict([line.split(" -> ") for line in data[2:]])

pair_count = Counter([x + y for x, y in zip(base, base[1:])])

for _ in range(40):
    new_pair_count = defaultdict(int)
    for pair, count in pair_count.items():
        insert = rules[pair]
        first_l, second_l = pair

        new_pair_count[first_l + insert] += count
        new_pair_count[insert + second_l] += count

    pair_count = new_pair_count

first_count = defaultdict(int)
second_count = defaultdict(int)

for pair, count in pair_count.items():
    first_l, second_l = pair
    first_count[first_l] += count
    second_count[second_l] += count

counts = {char: max(first_count[char], second_count[char]) for char in first_count.keys()}

print(max(counts.values()) - min(counts.values()))