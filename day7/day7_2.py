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

timelines_at_cell = [[0] * len(matrix[0]) for _ in range(len(matrix))]
timelines_at_cell[start[0]][start[1]] = 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if 0 <= i -1 < len(matrix) and 0 <= j < len(matrix[0]):
                num_timelines = timelines_at_cell[i-1][j]
                value = matrix[i-1][j]
                if value == 'S' or value == '|':
                    if matrix[i][j] == "^":
                        timelines_at_cell[i][j - 1] += num_timelines
                        timelines_at_cell[i][j + 1] += num_timelines
                        matrix[i][j-1] = "|"
                        matrix[i][j+1] = "|"
                    else:
                        timelines_at_cell[i][j] += num_timelines
                        matrix[i][j] = "|"

total_timelines = sum(timelines_at_cell[len(matrix) - 1])
print(f"{total_timelines=}")
