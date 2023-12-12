
# part 1
with open('input-1-1.txt', 'r') as lines:
    calibration_value = 0
    current_value = ""
    for line in lines:
        for i in range(len(line)):
            if line[i].isnumeric():
                current_value += str(line[i])
        if len(current_value) == 1:
            current_value += current_value
        calibration_value += int(current_value[0] + current_value[-1])
        current_value = ""
    print(calibration_value)


