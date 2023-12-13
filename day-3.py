
with open('input.txt', 'r') as lines:
    # {'467': [[0, (0, 2)], [1, (2, 4)]], }
    nums_coord = {}
    line_num_1 = 0
    line_num_2 = 0
    total_sum = 0
    current_num = ''
    current_coord = []
    for line in lines:
        for i in range(len(line)):
            if line[i].isnumeric():
                current_num += line[i]
                current_coord.append(str(i))
            else:
                if current_num != '':
                    if current_num not in nums_coord:
                        nums_coord[current_num] = [[line_num_1, (current_coord[0], current_coord[-1])]]
                    else:
                        nums_coord[current_num].append([line_num_1, (current_coord[0], current_coord[-1])])
                current_num = ''
                current_coord = []
        line_num_1 += 1
    print(nums_coord)

with open('input.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == ".":
                continue
            elif not line[i].isnumeric():
                for number, coordinates in nums_coord.items():
                    for coordinates_set in coordinates:
                        if line_num_2 - 1 == coordinates_set[0] or line_num_2 + 1 == coordinates_set[0]:
                            if (int(coordinates_set[1][0]) <= i <= int(coordinates_set[1][1])) or (i == int(coordinates_set[1][1]) + 1) or (i + 1 == int(coordinates_set[1][0])):
                                total_sum += int(number)
                                print(number, line[i])
                        if line_num_2 == coordinates_set[0]:
                            if i == int(coordinates_set[1][1]) + 1 or i + 1 == int(coordinates_set[1][0]):
                                total_sum += int(number)
                                print(number, line[i])
        line_num_2 += 1
    print('')
    print(total_sum)
