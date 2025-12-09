from shapely.geometry import Polygon
import time
t0 = time.time()

def calculate_size(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


input = []


def read_in_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            input.append([int(e) for e in line.split(",")])


read_in_file("day9_input.txt")
poly = Polygon(input)

size = len(input)

distances = []
for i in range(0, size):
    for j in range(0, size):
        if i != j and i > j:
            dist = calculate_size(input[i], input[j])
            distances.append((dist, input[i], input[j]))
distances.sort(key=lambda x: x[0], reverse=True)


def check_coords(coord1, coord2):
    smallest_x = min(coord1[0], coord2[0])
    largest_x = max(coord1[0], coord2[0])

    smallest_y = min(coord1[1], coord2[1])
    largest_y = max(coord1[1], coord2[1])

    poly2 = Polygon([(smallest_x, smallest_y), (smallest_x, largest_y), (largest_x, largest_y), (largest_x, smallest_y), (smallest_x, smallest_y)])
    return not poly2.within(poly)

i = 0
while check_coords(distances[i][1], distances[i][2]):
    i += 1

print(i, distances[i])

t1 = time.time()
total = t1-t0
print(total)
