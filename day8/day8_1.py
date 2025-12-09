import numpy as np
from utils import get_path

path = get_path()

connect = 1000
top_sizes = 3

coords = []
with open(path, 'r') as f:
    for l in f.readlines():
        l = l.strip()
        coords.append([int(k) for k in l.split(",")])

# print(coords)

coords = np.array(coords, np.uint64)
x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]
dist = np.sqrt((x - x[:, None]) ** 2 + (y - y[:, None]) ** 2 + (z - z[:, None]) ** 2)
np.fill_diagonal(dist, np.inf)

def find_closest(dist):
    ind = np.unravel_index(np.argmin(dist, axis=None), dist.shape)

    dist[ind[0], ind[1]] = np.inf
    dist[ind[1], ind[0]] = np.inf
    return ind


closest_combos = []


def describe_closest():
    closest = find_closest(dist)
    # print(closest, coords[closest[0]], coords[closest[1]])
    return closest


for i in range(connect):
    closest_combos.append(describe_closest())

closest_combos.sort(key=lambda x: x[0])
# print(closest_combos)
adjacency_list = {}

unique = set(list(zip(*closest_combos))[0])
unique.update(set(list(zip(*closest_combos))[1]))
for e in unique:
    adjacency_list[e] = set()
for combo in closest_combos:
    adjacency_list[combo[0]].add(combo[1])
    adjacency_list[combo[1]].add(combo[0])

# print(adjacency_list)


def find_islands(graph):
    visited = set()
    island_sizes = []
    for node in graph.keys():
        if node not in visited:
            current_island_size = 0
            stack = [node]
            visited.add(node)
            while stack:
                u = stack.pop()
                current_island_size += 1
                for v in graph.get(u, set()):
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            island_sizes.append(current_island_size)
    return island_sizes


islands = find_islands(adjacency_list)
islands.sort(reverse=True)
# print(islands)
prod = 1
for e in islands[:top_sizes]:
    prod *= e
print(prod)
