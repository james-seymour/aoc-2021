from utils import read_aoc_input, count_freq
from dataclasses import dataclass
import collections

# edges = [line.split("-") for line in read_aoc_input(12)]
edges = [line.split("-") for line in "start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end".split()]


def opposite(edge):
    ops = []
    for s,e in edges:
        if s == edge:
            ops.append(e)
        elif e == edge:
            ops.append(s)
    return ops




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

        dups = [item for item, count in collections.Counter(current.path).items() if count > 1]
        if True in [dup[0].islower() for dup in dups]:
            continue

        for new_n in successors(current):
            q.append(new_n)
    return all

print(len(search()))
# def search():
#     all = []
#     q = []
#     visited = set()
#     q.append(Node("start", ["start"]))
#     while q:
#         current = q.pop()

#         if current.v == "end":
#             all.append(current)

#         for new_n in opposite(current):
#             print(new_n)
#             # if new_n.v in visited:
#                 # continue
#             if sum([v[0].islower() for v in new_n.path]) > 2:
#                 continue
                
#             q.append(new_n)
 
#     return all



            







    




