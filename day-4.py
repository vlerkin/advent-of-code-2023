
with open('input.txt', 'r') as lines:
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
    print(total_points)

