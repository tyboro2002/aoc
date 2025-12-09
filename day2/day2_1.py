output = 0
with open("day2_input.txt") as f:
    for l in f.readlines():
        ranges = l.split(",")
        for range_ in ranges:
            splited = range_.split("-")
            first_item = splited[0]
            second_item = splited[1]
            for i in range(int(first_item), int(second_item)+1):
                str_i = str(i)
                if str_i[0:len(str_i)//2] == str_i[len(str_i)//2:] and len(str_i)%2 == 0:
                    output += i

print(output)