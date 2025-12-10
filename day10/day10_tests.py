from itertools import product

import numpy as np

from utils import get_path

path = get_path()

input = []

# toggelen is add mod 2 dus linear algebra over mod 2 (F2)
# convert to Ax = b (mod 2)
#   A = row for each light colum for each button Aij = 1 betekent dat button j light i toggeld
#   x = the parity of preses for buttons (even 0 of oneven 1)
#   b = target (verschil met de alles uit status)

# solven met gausian elimination
#   reduce met reduced row echelon form (swap 2 rows or add 2 rows)

# dit geeft welke buttons een vaste partiteit hebben en welke we mogen kiezen
#   pivot variable als eerste non zero entry in de RREF form een 1 is

def read_in_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().split(" ")
            # input.append([int(e) for e in line.split(",")])
            input.append(([1 if e == "#" else 0 for e in line[0][1:-1]], [[int(e) for e in k[1:-1].split(",")] for k in line[1:-1]], [int(e) for e in line[-1][1:-1].split(",")]))


read_in_file(path)
# print(input)


def prepare_machine_data(target_lights, button_combinations):
    N = len(target_lights)  # Number of lights
    num_buttons = len(button_combinations)

    # 1. Target Vector b
    target_b = np.array(target_lights, dtype=np.int8)

    # 2. Button Matrix A
    button_matrix_A = np.zeros((N, num_buttons), dtype=np.int8)

    for j, indices in enumerate(button_combinations):
        for i in indices:
            if 0 <= i < N:
                button_matrix_A[i, j] = 1

    return target_b, button_matrix_A, num_buttons


def find_rref_f2(M):
    rows, cols = M.shape
    pivot_row = 0
    pivot_cols = []

    for j in range(cols):
        if pivot_row >= rows:
            break

        i = pivot_row
        while i < rows and M[i, j] == 0:
            i += 1

        if i < rows:
            M[[pivot_row, i]] = M[[i, pivot_row]]
            pivot_cols.append(j)

            for k in range(rows):
                if k != pivot_row and M[k, j] == 1:
                    M[k, :] = (M[k, :] + M[pivot_row, :]) % 2
            pivot_row += 1

    return pivot_cols, pivot_row


def solve_machine(target_b, button_matrix_A, num_buttons):
    N = len(target_b)
    if N == 0:
        return 0

    augmented_matrix = np.hstack([button_matrix_A, target_b.reshape(-1, 1)])

    pivot_cols, rank = find_rref_f2(augmented_matrix)

    free_vars = [j for j in range(num_buttons) if j not in pivot_cols]
    k = len(free_vars)

    x_p = np.zeros(num_buttons, dtype=np.int8)
    for i, j in enumerate(pivot_cols):
        x_p[j] = augmented_matrix[i, -1]

    H_basis = []

    for j_free in free_vars:
        h_i = np.zeros(num_buttons, dtype=np.int8)
        h_i[j_free] = 1

        for i_pivot, j_pivot in enumerate(pivot_cols):
            h_i[j_pivot] = augmented_matrix[i_pivot, j_free]

        H_basis.append(h_i)

    min_presses = float('inf')

    for coeffs in product([0, 1], repeat=k):
        current_x = x_p.copy()
        for c, h in zip(coeffs, H_basis):
            if c == 1:
                current_x = (current_x + h) % 2
        weight = np.sum(current_x)
        min_presses = min(min_presses, weight)

    return min_presses


def solve_all_machines(input_data):
    total_min_presses = 0

    for i, (target_lights, button_combinations, _) in enumerate(input_data):
        target_b, button_matrix_A, num_buttons = prepare_machine_data(target_lights, button_combinations)

        min_presses = solve_machine(target_b, button_matrix_A, num_buttons)

        if min_presses == float('inf'):
            # print(f"Machine {i + 1} has no solution.")
            return -1

        total_min_presses += min_presses
        # print(f"Machine {i + 1} min presses: {min_presses}")

    return total_min_presses

print(f"Total Fewest Button Presses Required: {solve_all_machines(input)}")
