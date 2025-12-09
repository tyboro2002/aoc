from utils import get_path

path = get_path()

matrix = []
with open (path) as f:
    for line in f.readlines():
        line = line.strip()
        matrix.append([c for c in line])

valid = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        rolls = 0
        if matrix[i][j] == "@":
            for dx_val, dy_val in zip(dx, dy):
                if 0 <= i + dx_val < len(matrix) and 0 <= j + dy_val < len(matrix[0]):
                    value = matrix[i + dx_val][j + dy_val]
                    if value == "@":
                        rolls += 1
            if rolls < 4:
                valid += 1

print(valid)
