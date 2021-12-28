def get_lines_from_input():
    with open("input.txt") as file:
        return [line.strip() for line in file]


# Height map:
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# put numbers into array
def get_heightmap_and_dimensions():
    heightmap = [[int(s) for s in line] for line in get_lines_from_input()]
    return heightmap, len(heightmap), len(heightmap[0])


class Heightmap:
    def __init__(self):
        self.map, self.height, self.width = get_heightmap_and_dimensions()

    def get(self, y, x):
        return self.map[y][x]

    def get_neighbors(self, y, x):
        neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
        return [(y_n, x_n) for y_n, x_n in neighbors if 0 <= y_n < self.height and 0 <= x_n < self.width]

