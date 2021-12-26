def get_lines_from_input():
    with open("input.txt") as file:
        return [line.strip() for line in file]


#  0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


TEN_SIGNAL_DIGITS = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"}
}

UNIQUE_DIGITS = {1, 4, 7, 8}

UNIQUE_DIGITS_CHARS_LEN = {len(TEN_SIGNAL_DIGITS[d]): d for d in UNIQUE_DIGITS}

# Single entry
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf


def get_digits_and_signals_from_lines():
    input_lines = get_lines_from_input()
    for line in input_lines:
        digits, signals = line.split(" | ")
        yield digits.split(), signals.split()


def solve_digits(digits):
    solved = {}
    segment_map = {}

    for digit in digits:
        if len(digit) in UNIQUE_DIGITS_CHARS_LEN:
            digit_length = len(digit)
            solved[UNIQUE_DIGITS_CHARS_LEN[digit_length]] = set(digit)

    segment_map["a"] = list(solved[7] - solved[1])[0]

    for digit in digits:
        if len(digit) == 5 and set(digit).issuperset(solved[1]):
            # this means the digit is 3
            solved[3] = set(digit)
            break

    segment_map["g"] = list(solved[3] - solved[4] - {segment_map["a"]})[0]
    segment_map["d"] = list(solved[3] - solved[7] - {segment_map["g"]})[0]
    segment_map["e"] = list(solved[8] - solved[4] - solved[3])[0]
    segment_map["b"] = list(solved[4] - solved[1] - {segment_map["d"]})[0]

    for digit in digits:
        # get 2 and 5
        if len(digit) == 5:
            if segment_map["e"] in set(digit):
                solved[2] = set(digit)
            elif segment_map["b"] in set(digit):
                solved[5] = set(digit)

    # we now know 1, 2, 3, 4, 5, 7, 8, 9, and a, b, d, e, g
    segment_map["c"] = list(solved[2] - {segment_map["a"]} - {segment_map["d"]} - {segment_map["e"]} - {segment_map["g"]})[0]

    for digit in digits:
        if len(digit) == 6:
            if set(digit).issuperset(solved[4]):
                solved[9] = set(digit)
            elif segment_map["c"] not in set(digit):
                solved[6] = set(digit)
            elif segment_map["d"] not in set(digit):
                solved[0] = set(digit)
    return solved


def get_solved_numbers_from_digits(digits, signals):
    output = []

    solved_digits = solve_digits(digits)
    # get output from signals based on the solved digits
    for signal in signals:
        for i, s in solved_digits.items():
            if set(signal) == s:
                output.append(i)
                break
    return int("".join(str(i) for i in output))


total = 0
for digits, signals in get_digits_and_signals_from_lines():
    code = get_solved_numbers_from_digits(digits, signals)
    total += int(code)

print(total)
