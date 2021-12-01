
def read_input(day: int):
    with open(f"day_{day}_input.txt") as f:
        return f.readlines()

def parse_to_tuple(lines):
    return tuple(map(int, (lines)))

def parse_to_list(lines):
    return list(map(int, (lines)))