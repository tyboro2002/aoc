from utils import get_path

path = get_path()

height = 4
lines = []
operations = []

with open(path) as f:
    raw_lines = f.readlines()

for i, l in enumerate(raw_lines):
    if i < height:
        lines.append(l.rstrip('\n'))
    elif i == height:
        operations = [item for item in l.split() if item != ""]

max_width = max(len(l) for l in lines)
padded_lines = [l.ljust(max_width) for l in lines]

char_matrix = [list(col) for col in zip(*padded_lines)]


index = 0
temp = 0 if operations[index] == "+" else 1
sumed = 0
for i in range(len(char_matrix)):
    if all(element == ' ' for element in char_matrix[i]):
        index += 1
        sumed += temp
        temp = 0 if operations[index] == "+" else 1
    else:
        number = int("".join(char_matrix[i]))
        if operations[index] == "+":
            temp += number
        else:
            temp *= number

sumed += temp
print(f"Sum: {sumed}")
