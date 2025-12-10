from collections import deque
from utils import get_path

path = get_path()

input = []


def read_in_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().split(" ")
            input.append(([1 if e == "#" else 0 for e in line[0][1:-1]],
                          [[int(e) for e in k[1:-1].split(",")] for k in line[1:-1]],
                          [int(e) for e in line[-1][1:-1].split(",")]))


read_in_file(path)


def toggle(start, buttons):
    next_state = list(start)
    for button in buttons:
        next_state[button] = 1 - next_state[button]
    return next_state


def solve_machine(inp):
    target_lights = inp[0]
    button_combinations = inp[1]

    N = len(target_lights)
    start_state_list = [0] * N

    target_tuple = tuple(target_lights)
    start_tuple = tuple(start_state_list)

    if start_tuple == target_tuple:
        return 0

    queue = deque([(start_tuple, 0)])

    visited = {start_tuple}

    while queue:
        current_state_tuple, current_presses = queue.popleft()
        current_state = list(current_state_tuple)

        for button_indices in button_combinations:
            next_state = toggle(current_state, button_indices)
            next_state_tuple = tuple(next_state)

            if next_state_tuple == target_tuple:
                return current_presses + 1

            if next_state_tuple not in visited:
                visited.add(next_state_tuple)
                queue.append((next_state_tuple, current_presses + 1))
    return float('inf')


def solve_all_machines():
    start = 0
    for e in input:
        start += solve_machine(e)
    return start


print(solve_all_machines())
