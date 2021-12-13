from utils import read_aoc_input
import collections

edges = [line.split("-") for line in read_aoc_input(12)]

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

def search():
    all = []
    q = [Node("start", ["start"])]
    while q:
        current = q.pop()

        if current.v == "end":
            all.append(current.path)
            continue

        counts = collections.Counter(current.path)
        lowers = {k: v for k, v in counts.items() if k[0].islower()}

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