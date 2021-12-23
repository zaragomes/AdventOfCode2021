from collections import Counter


def get_input_from_file():
    with open("input.txt") as file:
        return [int(s) for s in file.read().strip().split(",")]


def get_crab_placement(with_summation=False):
    current_crabs = get_input_from_file()
    counter = Counter(current_crabs)

    min_pos = min(counter)
    max_pos = max(counter)
    # get fuel needed for crabs assembling at position 0
    if with_summation:
        current_sum = sum((interval*(interval + 1)/2) * num for interval, num in counter.items())
    else:
        current_sum = sum(interval * num for interval, num in counter.items())

    for pos in range(min_pos, max_pos):
        lowest_candidate = 0
        for interval, num in counter.items():
            if with_summation:
                lowest_candidate += (abs(interval - pos)*(abs(interval - pos) + 1)/2)*num
            else:
                lowest_candidate += abs(interval - pos)*num

        if lowest_candidate < current_sum:
            current_sum = lowest_candidate
    return current_sum


print(get_crab_placement(False))
