from collections import Counter

points_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
chunks_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
inv_chunk_pairs = {v: k for k, v in chunks_pairs.items()}
completion_points_map = {")": 1, "]": 2, "}": 3, ">": 4}


def get_lines_from_input():
    with open("input.txt") as file:
        return [list(line.strip()) for line in file]


def find_corruptions_and_incompletes():
    corruptions = Counter({x:0 for x in chunks_pairs.keys()})
    incomplete_stack = []
    for line in get_lines_from_input():
        stack = []
        for char in line:
            if char in chunks_pairs.values():
                stack.append(char)
            elif char in chunks_pairs.keys():
                latest = stack.pop()
                # if the previous character is a match
                if latest == chunks_pairs[char]:
                    continue
                else:
                    corruptions[char] += 1
                    stack = []
                    break

        # we've reached the end of the line, so the incomplete lines will still have
        if len(stack) > 0:
            incomplete_stack.append(stack)

    return corruptions, incomplete_stack


def calculate_corruptions():
    corruptions, incomplete_stack = find_corruptions_and_incompletes()
    total = 0
    for char, count in corruptions.items():
        total += points_map[char] * count
    return total


def get_total_points_of_missing_chars(incomplete_stack):
    totals = []
    for stack in incomplete_stack:
        total = 0
        while len(stack) > 0:
            total = (total * 5) + completion_points_map[inv_chunk_pairs[stack.pop()]]
        totals.append(total)
    return sorted(totals)










