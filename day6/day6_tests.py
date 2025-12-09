numbers = [64, 23, 314]
numbers = [51, 387, 215]


def transform(numbers, operation):
    temp = [str(n) for n in numbers]
    max_len = 0
    for i in range(len(temp)):
        if max_len < len(temp[i]):
            max_len = len(temp[i])
        temp[i] = [k for k in temp[i]]
    if operation == '+':
        for i in range(len(temp)):
            if len(temp[i]) < max_len:
                while len(temp[i]) < max_len:
                    temp[i].append("")

    if operation == '*':
        for i in range(len(temp)):
            if len(temp[i]) < max_len:
                while len(temp[i]) < max_len:
                    temp[i].insert(0, "")

    transposed_temp = list(zip(*temp))
    for i in range(len(transposed_temp)):
        transposed_temp[i] = int("".join(transposed_temp[i]))
    if operation == '+':
        return sum(transposed_temp)
    if operation == '*':
        temp = 1
        for number in transposed_temp:
            temp *= number
        return temp
    return transposed_temp


print(transform(numbers, '*'))
