
# part 1
with open('input-14.txt', 'r') as lines:
    line_count = 0
    # {1: [x1, x2, x3], 2: [x4, x5]}
    round_rock_coords = {}
    square_rock_coords = {}
    total_count = 0

    def move_round_rock(x_coord: int):
        round_keys = list(round_rock_coords.keys())
        square_keys = list(square_rock_coords.keys())
        all_keys = set(round_keys + square_keys)
        reverted_keys = sorted(all_keys, reverse=True)

        for line_num in reverted_keys:
            # find the nearest rock to move to
            # if there is nothing on this x coord, check next line, if the place for rock is found, break the loop
            if (round_rock_coords.get(line_num) is not None and x_coord in round_rock_coords[line_num]
                    or square_rock_coords.get(line_num) is not None and x_coord in square_rock_coords[line_num]):
                if round_rock_coords.get(line_num + 1) is not None:
                    round_rock_coords[line_num + 1].append(x_coord)
                    break
                else:
                    round_rock_coords[line_num + 1] = [x_coord]
                    break
            elif line_num == 1 and (x_coord not in round_rock_coords[line_num] or x_coord not in square_rock_coords[line_num]):
                if round_rock_coords.get(line_num) is not None:
                    round_rock_coords[line_num].append(x_coord)
                else:
                    round_rock_coords[line_num] = [x_coord]

    for line in lines:
        line_count += 1
        line.strip()
        if line_count == 1:
            for i in range(len(line)):
                if line[i] == 'O':
                    if line_count not in round_rock_coords:
                        round_rock_coords[line_count] = [i]
                    else:
                        round_rock_coords[line_count].append(i)
                elif line[i] == '#':
                    if line_count not in square_rock_coords:
                        square_rock_coords[line_count] = [i]
                    else:
                        square_rock_coords[line_count].append(i)
        else:
            for i in range(len(line)):
                if line[i] == 'O':
                    move_round_rock(i)
                if line[i] == '#':
                    if line_count not in square_rock_coords:
                        square_rock_coords[line_count] = [i]
                    else:
                        square_rock_coords[line_count].append(i)

    for line_num, coordinates in round_rock_coords.items():
        total_count += (line_count - line_num + 1)*len(coordinates)
    print(total_count)
