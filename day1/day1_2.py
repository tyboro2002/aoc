start = 50
zero_counts = 0


def get_next(start, motion):
    sign = 1
    zeros = 0
    if motion[0] == "L":
        sign = -1
    value = int(motion[1:])
    for i in range(0, value):
        start = (start + sign) % 100
        if start == 0:
            zeros += 1
    return start, zeros


with open("day1_1_input.txt", "r") as f:
    for line in f.readlines():
        old = start
        start, zeros = get_next(start, line.strip())
        zero_counts += zeros
        # if start == 0:
        #     zero_counts += 1
        # print(start, zeros, zero_counts)

print(zero_counts)
