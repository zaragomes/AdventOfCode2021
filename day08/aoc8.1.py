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


TEN_SIGNAL_PATTERNS = {
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

UNIQUE_DIGITS_CHARS_LEN = {len(TEN_SIGNAL_PATTERNS[d]) for d in UNIQUE_DIGITS}
print(UNIQUE_DIGITS_CHARS_LEN)

# Single entry
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf


def get_patterns_and_signals_from_lines():
    input_lines = get_lines_from_input()
    for line in input_lines:
        patterns, signals = line.split(" | ")
        yield patterns.split(), signals.split()


def count_certain_numbers():
    count = 0
    for patterns, signals in get_patterns_and_signals_from_lines():
        print(patterns, signals)
        for signal in signals:
            if len(signal) in UNIQUE_DIGITS_CHARS_LEN:
                count = count + 1
    return count


print(count_certain_numbers())
