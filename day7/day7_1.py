from utils import get_path

path = get_path()

matrix = []
with open(path) as f:
    for line in f.readlines():
        line = line.strip()
        matrix.append([c for c in line])


def find_s(matrix):
    for i in range(len(matrix)):
        if 'S' in matrix[i]:
            return i, matrix[i].index('S')

start = find_s(matrix)

split_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if 0 <= i -1 < len(matrix) and 0 <= j < len(matrix[0]):
                value = matrix[i -1][j ]
                if value == 'S' or value == '|':
                    if matrix[i][j] == "^":
                        split_count += 1
                        matrix[i][j-1] = "|"
                        matrix[i][j+1] = "|"
                    else:
                        matrix[i][j] = "|"

print(f"{split_count=}")
