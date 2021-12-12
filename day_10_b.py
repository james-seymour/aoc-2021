from utils.data import read_aoc_input
from functools import reduce
data = read_aoc_input(10)


points = {")": 1, "]": 2, "}": 3, ">": 4}

def check_balanced(my_string):
    stack = []
    match = { '(': ')', '{': '}', '[': ']', '<': '>' }
    for i, char in enumerate(my_string):
        if char in match.keys():
            stack.append(char)
            continue
        
        r = stack.pop()
        if char != match[r]:
            return i, char

    if len(stack) == 0:
        return True

    return None, list(map(match.get, stack))

totals = []
for line in data:
    code, inv_stack = check_balanced(line)
    if len(inv_stack) > 1:
        inv_stack.reverse()

    if code is not None:
        continue

    ps = [0] + list(map(points.get, inv_stack))
    total = reduce(lambda x,y : x*5 + y, ps)
    totals.append(total)

totals.sort()
print(totals[int(len(totals)/2)])


    

