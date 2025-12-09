from utils import get_path

path = get_path()

height = 4
matrix = []
operations = []
with open(path) as f:
    for l in f.readlines():
        l = l.strip()
        # print(numbers)
        if height:
            numbers = [int(item) for item in l.split(" ") if item != ""]
            matrix.append(numbers)
            height -= 1
        else:
            operations = [item for item in l.split(" ") if item != ""]
# print(height)
# print(matrix)
transposed_matrix = list(zip(*matrix))  # unpack the list zip it and pack it back together
# print(transposed_matrix)
sumed = 0
for line, option in zip(transposed_matrix, operations):
    if option == "+":
        temp = sum(numbers)
    else:
        temp = 1
        for number in line:
            temp *= number
    sumed += temp

print(sumed)
