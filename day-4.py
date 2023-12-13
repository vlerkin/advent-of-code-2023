
# part 1
"""with open('input.txt', 'r') as lines:
    total_points = 0
    for line in lines:
        card_points = 0
        winning_nums, card_nums = line.strip().split(": ")[1].split(" | ")
        winning_nums = winning_nums.split()
        card_nums = card_nums.split()
        nums = set(card_nums).intersection(set(winning_nums))
        for i in range(len(nums)):
            if i == 0:
                card_points = 1
            else:
                card_points *= 2
        total_points += card_points
    print(total_points)"""

# part 2
with open('input.txt', 'r') as lines:
    num_card_instances = {}
    card_number = 0
    for line in lines:
        card_number += 1
        if card_number not in num_card_instances:
            num_card_instances[card_number] = 1
        else:
            num_card_instances[card_number] += 1
        winning_nums, card_nums = line.strip().split(": ")[1].split(" | ")
        winning_nums = winning_nums.split()
        card_nums = card_nums.split()
        nums = set(card_nums).intersection(set(winning_nums))
        print(num_card_instances[card_number])
        for j in range(num_card_instances[card_number]):
            for i in range(len(nums)):
                if (card_number + i + 1) not in num_card_instances:
                    num_card_instances[card_number + i + 1] = 1
                else:
                    num_card_instances[card_number + i + 1] += 1
    print(num_card_instances)
    print(sum(num_card_instances.values()))

