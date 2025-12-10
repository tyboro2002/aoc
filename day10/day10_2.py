from pulp import LpProblem, LpVariable, LpMinimize, value, PULP_CBC_CMD

from utils import get_path

path = get_path()

input = []


def read_in_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().split(" ")
            light_state = [1 if e == "#" else 0 for e in line[0][1:-1]]
            button_combos = [[int(e) for e in k[1:-1].split(",")] for k in line[1:-1]]
            target_lights = [int(e) for e in line[-1][1:-1].split(",")]
            input.append((light_state, button_combos, target_lights))


try:
    read_in_file(path)
except FileNotFoundError:
    print(f"Warning: Could not read file at {path}. Input list may be empty.")
except Exception as e:
    print(f"Error reading file: {e}")


def solve_ilp_system(reduced_buttons, reduced_target):
    T_prime = reduced_target
    N_prime = len(T_prime)
    K_prime = len(reduced_buttons)

    if not K_prime:
        return 0 if all(t == 0 for t in T_prime) else float('inf')

    model = LpProblem("Minimum_Button_Presses", LpMinimize)
    C = [LpVariable(f"C_{j}", lowBound=0, cat='Integer') for j in range(K_prime)]
    model += sum(C), "Total_Presses"

    for i in range(N_prime):
        light_expression = []
        for j in range(K_prime):
            if i in reduced_buttons[j]:
                light_expression.append(C[j])

        model += sum(light_expression) == T_prime[i], f"Light_Constraint_{i}"

    try:
        model.solve(PULP_CBC_CMD(msg=0))  # msg=0 suppresses solver output
    except Exception:
        return float('inf')

    if model.status == 1:  # 1 means LpStatus.Optimal
        total_presses = sum(value(C[j]) for j in range(K_prime))
        return total_presses

    else:
        return float('inf')


def solve_machine(inp):
    target_lights = list(inp[2])  # Make a mutable copy
    button_combinations = inp[1]

    N = len(target_lights)
    K = len(button_combinations)

    light_to_buttons = [[] for _ in range(N)]
    for k in range(K):
        for light_index in button_combinations[k]:
            light_to_buttons[light_index].append(k)

    fixed_counts = [0] * K
    total_fixed_presses = 0

    while True:
        variables_fixed_in_this_pass = 0

        for i in range(N):
            if target_lights[i] == 0:
                continue

            unfixed_affecting_buttons = [k for k in light_to_buttons[i] if fixed_counts[k] == 0]

            if len(unfixed_affecting_buttons) == 1:
                k = unfixed_affecting_buttons[0]
                required_presses = target_lights[i]

                if required_presses < 0:
                    return float('inf')

                fixed_counts[k] = required_presses
                total_fixed_presses += required_presses
                variables_fixed_in_this_pass += 1

                for j in range(N):
                    if k in light_to_buttons[j]:
                        target_lights[j] -= required_presses

        if variables_fixed_in_this_pass == 0:
            break

    if any(t < 0 for t in target_lights):
        return float('inf')

    if all(t == 0 for t in target_lights):
        return total_fixed_presses

    remaining_button_indices = [k for k in range(K) if fixed_counts[k] == 0]
    remaining_lights_indices = [i for i, t in enumerate(target_lights) if t > 0]

    if not remaining_button_indices:
        return float('inf')

    old_to_new_light_map = {old_i: new_i for new_i, old_i in enumerate(remaining_lights_indices)}

    reduced_target = [target_lights[i] for i in remaining_lights_indices]
    reduced_buttons = []

    for old_k in remaining_button_indices:
        old_button = button_combinations[old_k]

        new_button = [old_to_new_light_map[light_index]
                      for light_index in old_button
                      if light_index in remaining_lights_indices]

        if new_button:
            reduced_buttons.append(new_button)

    if not reduced_buttons and any(t > 0 for t in reduced_target):
        return float('inf')

    if not reduced_buttons and all(t == 0 for t in reduced_target):
        return total_fixed_presses

    result = solve_ilp_system(reduced_buttons, reduced_target)

    if result == float('inf'):
        return float('inf')
    else:
        return total_fixed_presses + result


def solve_all_machines():
    start = 0
    for e in input:
        curr = solve_machine(e)
        # print(int(curr) if curr != float('inf') else "inf")
        if curr != float('inf'):
            start += int(curr)
    return start


sol = solve_all_machines()
print(f"Total Minimum Presses: {int(sol) if sol != float('inf') else 'inf'}")
