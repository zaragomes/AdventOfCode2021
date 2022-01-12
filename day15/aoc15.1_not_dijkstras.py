from typing import List, Optional, Tuple


def get_lines_from_input():
    with open("example.txt") as file:
        return [line.strip() for line in file]


# put numbers into array
def get_risk_map():
    riskmap = [[int(s) for s in line] for line in get_lines_from_input()]
    return riskmap, len(riskmap), len(riskmap[0])


class RiskMap:
    def __init__(self):
        self.map, self.height, self.width = get_risk_map()
        self.start = (0, 0)
        self.end = (self.height - 1, self.width - 1)

    def get(self, y, x):
        return self.map[y][x]

    def get_neighbors(self, y, x):
        neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
        return [(y_n, x_n) for y_n, x_n in neighbors if 0 <= y_n < self.height and 0 <= x_n < self.width]

    def is_eligible(self, node, current_path):
        eligible = False
        if node == self.start:
            return False
        if node not in current_path:
            return True
        return eligible

    def calculate_lowest_risk(self,
                              neighbor,
                              current_score: int,
                              current_path: Optional[Tuple[str]] = None,
                              lowest_path: Optional[int] = None):

        neighbors = riskmap.get_neighbors(neighbor[0], neighbor[1])

        if current_path is None:
            current_path = []
        if current_score is None:
            current_score = 0

        for adjacent in neighbors:

            if riskmap.is_eligible(adjacent, current_path):
                new_score = current_score + riskmap.get(adjacent[0], adjacent[1])
                if lowest_path is not None:
                    if new_score > lowest_path:
                        continue

                new_path = current_path + [adjacent]

                if adjacent == riskmap.end:
                    if lowest_path is None or lowest_path > new_score:
                        lowest_path = new_score
                else:
                    lowest_path = self.calculate_lowest_risk(adjacent, new_score, new_path, lowest_path)

        return lowest_path


print("start")
riskmap = RiskMap()
path = riskmap.calculate_lowest_risk(riskmap.start, 0)
print(path)

