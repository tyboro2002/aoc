sum = 0
with open('day3_test.txt') as f:
    for l in f.readlines():
        l = l.strip()
        list_all = [int(k) for k in l[:-1]]
        m = max(list_all)
        sum += int(str(m) + str(max([int(k) for k in l[list_all.index(m)+1:]])))

print(sum)