start = 50
zero_counts = 0


def get_next(start, motion):
    sign = 1
    if motion[0] == "L":
        sign = -1
    value = int(motion[1:])
    return (start + sign * value) % 100


with open("day1_1_input.txt", "r") as f:
    for line in f.readlines():
        start = get_next(start, line.strip())
        if start == 0:
            zero_counts += 1

print(zero_counts)
