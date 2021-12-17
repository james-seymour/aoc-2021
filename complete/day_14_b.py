from collections import defaultdict, Counter

with open("day_14_input.txt") as f:
    data = [line.strip() for line in f.readlines()]

base = data[0]
rules = dict([line.split(" -> ") for line in data[2:]])

pair_count = Counter([x + y for x, y in zip(base, base[1:])])
polymer_count = Counter(base)

for _ in range(40):
    new_pair_count = defaultdict(int)
    for pair, count in pair_count.items():
        insert = rules[pair]
        first_l, second_l = pair

        new_pair_count[first_l + insert] += count
        new_pair_count[insert + second_l] += count
        polymer_count[insert] += count

    pair_count = new_pair_count

print(max(polymer_count.values()) - min(polymer_count.values()))