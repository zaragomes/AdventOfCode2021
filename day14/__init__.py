from collections import Counter


def get_lines_from_input():
    with open("input.txt") as file:
        return [(line.strip()) for line in file]


def get_template_and_instructions_from_lines():
    input_lines = get_lines_from_input()
    template = list(input_lines[0])
    instructions = {}
    for l in input_lines:
        if " -> " in l:
            parts = l.split(" -> ")
            instructions[parts[0]] = parts[1]
    return template, instructions


# Part 1 Brute force
# def daily_polymer_growth(template, instructions):
#     match_index_counter = Counter()
#     new_polymer = ""
#     for i in range(0, len(template)-1):
#         polymer_key = template[i] + template[i+1]
#         if polymer_key in instructions.keys():
#             polymer_val = instructions[polymer_key]
#             match_index_counter[i+1] = True
#             if match_index_counter[i]:
#                 new_polymer += polymer_val + template[i+1]
#             else:
#                 new_polymer += template[i] + polymer_val + template[i+1]
#     return new_polymer

# converting the input polymer into strings of 2 characters, and getting the count of overlapping characters
def convert_polymer_into_couples(template):
    polymer_couples = Counter()
    overlaps = Counter()
    for i in range(0, len(template)-1):
        first_char = str(template[i])
        second_char = str(template[i+1])
        joint = first_char + second_char
        polymer_couples[joint] += 1
        if i != len(template)-2:
            overlaps[template[i+1]] += 1
    return polymer_couples, overlaps


# daily growth.
def daily_polymer_growth(template_couples, instructions, overlaps):
    new_template_couples = template_couples.copy()
    for template_couple, count in template_couples.items():
        if count > 0:
            if instructions[template_couple]:
                insert = instructions[template_couple]
                new_template_couples[(str(template_couple[0]) + str(insert))] += count
                new_template_couples[(str(insert) + str(template_couple[1]))] += count
                new_template_couples[(template_couple)] -= count
                if new_template_couples[(template_couple)] == 0:
                    del new_template_couples[(template_couple)]
                overlaps[insert] += count
            else:
                new_template_couples[template_couple.keys()] = template_couple.values()
    return new_template_couples, overlaps


def polymer_growth_after_days(days):
    template, instructions = get_template_and_instructions_from_lines()
    new_template_couples = Counter()
    instruction_couples = Counter(instructions)
    template_couples, overlaps = convert_polymer_into_couples(template)

    while days > 0:
        new_template_couples, overlaps = daily_polymer_growth(template_couples, instruction_couples, overlaps)
        template_couples = new_template_couples
        days -= 1

    return new_template_couples, overlaps


def get_totals(template, overlaps):
    totals = Counter()
    for template_couple, count in template.items():
        totals[template_couple[0]] += count
        totals[template_couple[1]] += count
    for overlap, count in overlaps.items():
        if totals[overlap] - count > 0:
            totals[overlap] -= count
    return totals


days = 40
new_polymer, overlapping_elements = polymer_growth_after_days(days)
totals = get_totals(new_polymer, overlapping_elements)
most_common = max(Counter(totals).values())
least_common = min(Counter(totals).values())
print(most_common - least_common)


