import re


# part 1

"""with open('input-1-1.txt', 'r') as lines:
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
    print(calibration_value)"""
# part 2
with open('input-1-1.txt', 'r') as lines:
    calibration_value = 0
    num_to_word = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                   'eight': '8', 'nine': '9'}
    for line in lines:
        current_value = ''
        for i in range(len(line)):
            if line[i].isnumeric():
                current_value += line[i]
            else:
                for word in num_to_word.keys():
                    if (i + len(word)) <= len(line) and line[i:i+len(word)] == word:
                        current_value += num_to_word[word]
        if len(current_value) == 1:
            current_value += current_value
        calibration_value += int(current_value[0] + current_value[-1])
        print(current_value[0] + current_value[-1])
    print(calibration_value)



