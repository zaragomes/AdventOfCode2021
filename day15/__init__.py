from typing import Tuple
from dataclasses import dataclass, field
import heapq


def get_lines_from_input():
    with open("input.txt") as file:
        return [line.strip() for line in file]


# put numbers into array
def get_risk_map():
    riskmap = [[int(s) for s in line] for line in get_lines_from_input()]
    return riskmap, len(riskmap), len(riskmap[0])


def get_expanded_risk_map():
    riskmap, width, height = get_risk_map()
    expanded_riskmap = [[0 for c in range(5 * width)] for r in range(5 * height)]
    for i in range(0, len(riskmap)):
        for j in range(0, len(riskmap[0])):
            for m in range(0, 5):
                if riskmap[i][j] + m > 9:
                    expanded_riskmap[i][m*width + j] = riskmap[i][j] + m - 9
                else:
                    expanded_riskmap[i][m*width + j] = riskmap[i][j] + m
    for i in range(0, len(riskmap)):
        for j in range(0, len(expanded_riskmap[0])):
            for n in range(0, 5):
                if expanded_riskmap[i][j] + n > 9:
                    expanded_riskmap[n * height + i][j] = expanded_riskmap[i][j] + n - 9
                else:
                    expanded_riskmap[n * height + i][j] = expanded_riskmap[i][j] + n

    return expanded_riskmap, len(expanded_riskmap), len(expanded_riskmap[0])


@dataclass(order=True)
class Vertex:
    distance: int
    position: Tuple[int, int] = field(compare=False)

    def __str__(self):
        return f"{self.position}@d={self.distance}"


class RiskMap:
    def __init__(self, expanded=False):
        self.expanded = expanded
        if not expanded:
            self.map, self.height, self.width = get_risk_map()
        else:
            self.map, self.height, self.width = get_expanded_risk_map()
        self.start = (0, 0)
        self.end = (self.height - 1, self.width - 1)
        self.pq = [Vertex(0, (0, 0))]

    def get(self, y, x):
        return self.map[y][x]

    def get_neighbors(self, y, x):
        neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
        return [(y_n, x_n) for y_n, x_n in neighbors if 0 <= y_n < self.height and 0 <= x_n < self.width]

    def is_eligible(self, node, seen):
        eligible = False
        if node == self.start:
            return False
        if node not in seen:
            return True
        return eligible

    def calculate_lowest_risk(self):
        seen = {(0, 0): 0}
        while self.pq:
            n = heapq.heappop(self.pq)
            if n.position == self.end:
                print(f"we have reached our destination with {len(seen)} elements visited")
                break

            neighbors = self.get_neighbors(n.position[0], n.position[1])
            for adjacent in neighbors:
                if self.is_eligible(adjacent, seen):
                    add = Vertex(self.get(adjacent[0], adjacent[1]) + n.distance, (adjacent[0], adjacent[1]))
                    seen[add.position] = add.distance
                    heapq.heappush(self.pq, add)

        print(f"Found destination {seen[self.end]}")