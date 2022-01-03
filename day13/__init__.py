from collections import Counter
# for each line in input, plot the coordinates


def get_lines_from_input():
    with open("input.txt") as file:
        return [(line.strip()) for line in file]


def get_dots_and_instructions_from_lines():
    input_lines = get_lines_from_input()
    instr = []
    points = []
    for line in input_lines:
        if "," in line:
            x1y1 = tuple(int(a) for a in line.split(","))
            points.append(x1y1)
        elif "fold" in line:
            test = line.split(" ")
            instr.append(test[2])
    x_list = [x1y1[0] for x1y1 in points]
    y_list = [x1y1[1] for x1y1 in points]
    return Counter(points), max(x_list) + 1, max(y_list) + 1, instr


class Paper:
    def __init__(self):
        self.points_counter, self.width, self.height, self.instr = get_dots_and_instructions_from_lines()

    def fold_along_axis(self, axis, unit):
        if axis == "x":
            # if total width is 15 and fold happens at 9
            # we want to add 9 + 6 to 9 - 6, 9 + 5, 9 - 5. so 15 gets added to 3, 14 gets added to 4
            delta = self.width - unit
            # fold left
            for x in range(delta):
                for y in range(self.height):
                    if self.points_counter[(unit + x, y)] + self.points_counter[(unit - x, y)] > 0:
                        self.points_counter[(unit - x, y)] = 1
                        del(self.points_counter[(unit + x, y)])
            self.width = unit
        if axis == "y":
            delta = self.height - unit
            for x in range(self.width):
                for y in range(delta):
                    if self.points_counter[(x, unit + y)] + self.points_counter[(x, unit - y)] > 0:
                        self.points_counter[(x, unit - y)] = 1
                        del (self.points_counter[(x, unit + y)])
            self.height = unit




