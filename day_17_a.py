from typing import List, Tuple
from utils import read_aoc_input

target_x = range(282, 315)
target_y = range(-80, -44)

# assert x_vel > 0 (therefore always just -= 1 (unless 0))
# y_vel -= 1 each time


velocity = int

def follow_trajectory(i_x_vel, i_y_vel, step_count=4000) -> List[Tuple[int, int]]:
    x, y = 0, 0
    x_vel, y_vel = i_x_vel, i_y_vel
    steps = []
    for step in range(step_count):
        x += x_vel
        y += y_vel
        if x_vel != 0:
            x_vel -= 1
        y_vel -= 1
        steps.append((x, y))

    return steps

heights = []
for x_vel in range(0, 400):
    for y_vel in range(-100, 100):
        traject = follow_trajectory(x_vel, y_vel)
        if any([x in target_x and y in target_y for x, y in traject]):
            heights.append((x_vel,y_vel))

print(len(heights))
            


