from utils import get_path

path = get_path()

with open(path, 'r') as f:
    encountered_empty = False
    ranges = []
    fresh = 0
    for line in f.readlines():
        line = line.strip()
        if line == "":
            encountered_empty = True
        elif encountered_empty:
            pass
        else:
            ranges.append(range(int(line.split('-')[0]), int(line.split('-')[1]) + 1))


def calculate_unique_length(ranges):
    events = []
    for r in ranges:
        events.append((r.start, 1))
        events.append((r.stop, -1))
    events.sort()
    total_unique_count = 0
    open_ranges_count = 0
    last_position = 0
    for position, type in events:
        if open_ranges_count > 0:
            total_unique_count += position - last_position
        open_ranges_count += type
        last_position = position
    return total_unique_count


unique_count = calculate_unique_length(ranges)
print(unique_count)
