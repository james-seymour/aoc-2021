from re import A
from utils import read_aoc_input, count_freq, dict_map_vals
from dataclasses import dataclass
import collections

from utils.builtins import dict_map_keys

edges = [line.split("-") for line in read_aoc_input(12)]
# edges = [line.split("-") for line in "start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end".split()]


def successors(node):
    a = []
    for s, e in edges:
        if s == node.v:
            a.append(Node(e, node.path.copy() + [e]))
        if e == node.v:
            a.append(Node(s, node.path.copy() + [s]))    

    return a

class Node:
    def __init__(self, v, path):
        self.v = v
        self.path = path

    def __repr__(self):
        return f"{self.v}, {self.path}"

def edge_is_lower(edge):
    return edge[0].islower()

def parse_dups(dups):
    print(dups)
    if len(dups) == 1:
        if dups[0][1] > 2:
            return True
        else:
            return False
    if any([count >= 3 for e, count in dups]):
        return True

def search():
    all = []
    q = []
    start = Node("start", ["start"])
    q.append(start)
    while q:
        current = q.pop()

        if current.v == "end":
            all.append(current.path)
            continue

        counts = collections.Counter(current.path)
        yeet = []
        for k, v in counts.items():
            if k[0].islower():
                yeet.append((k,v))
        lowers = dict(yeet)

        if counts["start"] > 1 or counts["end"] > 1:
            continue
        if sum([count > 1 for count in lowers.values()]) > 1:
            continue
        if any([count > 2 for count in lowers.values()]):
            continue
        for new_n in successors(current):
            q.append(new_n)

    return all

print(len(search()))