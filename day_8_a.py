from utils import *
from collections import defaultdict

data = read_aoc_input(8)
data = [line.split("|")[1] for line in data]
data = [line.split(" ")[1:] for line in data]
lens = [2, 4, 3, 7]
stored = defaultdict(int)

for line in data:
    for word in line:
        if len(word) in lens:
            stored[len(word)] += 1

print(sum(stored.values()))

            
