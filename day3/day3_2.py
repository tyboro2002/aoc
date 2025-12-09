sum = 0
amount = 12
with open('day3_input.txt') as f:
    for l in f.readlines():
        l = l.strip()
        list_all = [int(k) for k in l]
        m = max(list_all[:-(amount-1)])
        list_all = list_all[list_all.index(m)+1:]
        numbers = []
        # print(m, list_all.index(m)+1, list_all[list_all.index(m)+1:-(amount-1)])
        numbers.append(str(m))
        for i in range(1, amount-1):
            # print(m, -(amount - 1 - i))
            # print(list_all[:-(amount-1-i)])
            m = max([int(k) for k in list_all[:-(amount-1-i)]])
            list_all = list_all[list_all.index(m)+1:]
            # print(m,-(amount-1-i) )
            numbers.append(str(m))
        # print(int("".join(numbers+[str(max(list_all))])))
        sum += int("".join(numbers+[str(max(list_all))]))

print(sum)