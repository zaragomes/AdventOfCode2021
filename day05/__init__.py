from collections import Counter
# for each line in input, plot the coordinates
field = []


def get_lines_from_input():
    with open("input.txt") as file:
        return [(line.strip()) for line in file]


def get_coordinates_from_lines():
    input_lines = get_lines_from_input()
    for line in input_lines:
        start, end = line.split(" -> ")
        x1y1 = tuple(int(a) for a in start.split(","))
        x2y2 = tuple(int(a) for a in end.split(","))
        yield x1y1, x2y2


# return the count of danger zones in the field
def count_danger_zones(inc_diagonals=False):
    counter = Counter()
    for x1y1, x2y2 in get_coordinates_from_lines():
        (x1, y1), (x2, y2) = x1y1, x2y2
        if x1 == x2:
            y_start, y_end = (y1, y2) if y2 > y1 else (y2, y1)
            for y in range(y_start, y_end + 1):
                counter[(x1, y)] += 1
        elif y1 == y2:
            x_start, x_end = (x1, x2) if x2 > x1 else (x2, x1)
            for x in range(x_start, x_end + 1):
                counter[(x, y1)] += 1
        elif inc_diagonals:
            (x_start, x_end), (y_start, y_end) = ((x1, x2), (y1, y2)) if x2 > x1 else ((x2, x1), (y2, y1))
            x_index = 0
            if y_start > y_end:
                range_direction = -1
            else:
                range_direction = 1
            for x in range(x_start, x_end + 1):
                y_index = 0
                for y in range(y_start, y_end + range_direction, range_direction):
                    if x_index == y_index:
                        counter[(x, y)] += 1
                    y_index += 1
                x_index += 1

    return sum(1 for count in counter.values() if count > 1)



