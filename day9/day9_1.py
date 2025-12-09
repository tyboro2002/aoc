def calculate_size(corner1, corner2):
    return (abs(corner1[0] - corner2[0])+1) * (abs(corner1[1] - corner2[1])+1)

input = []
def read_in_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            input.append([int(e) for e in line.split(",")])

# print(calculate_size((2,5), (9,7)))
read_in_file("day9_input.txt")
print(input)
# print(calculate_size(input[0], input[1]))

size = len(input)
max_distance = 0
for i in range(0, size):
    for j in range(0, size):
        if i != j and i>j:
            dist = calculate_size(input[i], input[j])
            if dist > max_distance:
                max_distance = dist

print(max_distance)

