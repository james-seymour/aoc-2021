from collections import Counter

with open("day_14_input.txt") as f:
    data = [line.strip() for line in f.readlines()]

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
print(base)

counter = Counter(base)

print(max(counter.values()) - min(counter.values()))