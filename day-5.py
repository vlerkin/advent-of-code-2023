
# part 1
with open('input.txt', 'r') as lines:
    line_num = 0
    seed_nums = []
    seed_to_location = {}
    numb_of_conversions = 0
    seed_mapping_copy = []

    def map_source_to_destination(source: int, destination: int, target: int):
        return target - (source - destination)

    for line in lines:
        line = line.strip()
        if line_num == 0:
            seed_nums = line.split(": ")[1].split()
            for seed_num in seed_nums:
                seed_to_location[seed_num] = [int(seed_num)]
        else:
            if line == '':
                numb_of_conversions += 1
                seed_mapping_copy = list(seed_to_location.keys())
                continue
            elif not line[0].isnumeric():
                continue
            else:
                destination_num, source_num, range_length = line.split()

                destination_num = int(destination_num)
                source_num = int(source_num)
                range_length = int(range_length)

                for seed_num, target_nums in seed_to_location.items():
                    target_num = target_nums[-1]
                    if seed_num in seed_mapping_copy and source_num <= target_num <= (source_num + range_length):
                        mapped_num = map_source_to_destination(source_num, destination_num, target_num)
                        seed_to_location[seed_num].append(mapped_num)
                        seed_mapping_copy.remove(seed_num)




        line_num += 1
    location_nums = []
    for items in seed_to_location.values():
        location_nums.append(items[-1])
    print(min(location_nums))
