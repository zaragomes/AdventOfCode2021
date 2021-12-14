from collections import Counter


def get_input_from_file():
    with open("input.txt") as file:
        return [int(s) for s in file.read().strip().split(",")]


def get_fish_states(days):
    current_fish_list = get_input_from_file()
    counter = Counter(current_fish_list)

    for day in range(days):
        new_counter = Counter()
        new_fish = 0
        for interval, count in counter.items():
            if interval == 0:
                new_counter[6] += count
                new_fish = count
            else:
                new_counter[interval - 1] += count
        new_counter[8] = new_fish
        counter = new_counter
    return counter


total = sum((get_fish_states(256).values()))
print(total)