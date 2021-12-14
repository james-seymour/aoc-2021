from utils import read_aoc_input
from collections import Counter, defaultdict

data = read_aoc_input(14)

base = data[0].strip()
rules = dict([line.split(" -> ") for line in data[2:]])

for _ in range(10): 
    seq = list(base)
    res = []
    for first, second in zip(seq, seq[1:]):
        insert = rules[first + second]
        res.append(first)
        res.append(insert)

    res.append(seq[-1])
    base = "".join(res)

counter = Counter(base)

print(max(counter.values()) - min(counter.values()))
