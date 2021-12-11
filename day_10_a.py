from utils.data import read_aoc_input

data = read_aoc_input(10)

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

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

    return None, None

t = 0 
for i, l in enumerate(data):
    i, char = check_balanced(l)
    if i is None: continue
    t += points[char]

print(t)