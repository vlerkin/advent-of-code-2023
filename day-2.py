
# part 1
with open('input.txt', 'r') as lines:
    start_config = {'red': 12, 'green': 13, 'blue': 14}
    games = []
    num_game = 1
    for line in lines:
        game = line.strip().split(": ")[1].split("; ")
        num_subsets = 0
        num_good_subsets = 0
        for subset in game:
            num_subsets += 1
            subset_config = {'red': 0, 'green': 0, 'blue': 0}
            rounds = subset.split(", ")
            for round in rounds:
                clean_round = round.split()
                subset_config[clean_round[1]] += int(clean_round[0])
            if all(subset_config[key] <= start_config[key] for key in start_config):
                num_good_subsets += 1
        if num_subsets == num_good_subsets:
            games.append(num_game)
        num_game += 1
    print(sum(games))
