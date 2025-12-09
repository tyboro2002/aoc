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
            number = int(line)
            for r in ranges:
                if number in r:
                    fresh += 1
                    break
        else:
            ranges.append(range(int(line.split('-')[0]), int(line.split('-')[1])+1))

print(fresh)
