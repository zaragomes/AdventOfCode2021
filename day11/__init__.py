
def get_lines_from_input():
    with open("input.txt") as file:
        return [line.strip() for line in file]

# Octopus map:
# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526


# put numbers into array
def get_octopus_energy_map():
    octomap = [[int(s) for s in line] for line in get_lines_from_input()]
    return octomap, len(octomap), len(octomap[0])


class OctoMap:
    def __init__(self):
        self.map, self.height, self.width = get_octopus_energy_map()

    def get(self, y, x):
        return self.map[y][x]

    def get_neighbors(self, y, x):
        neighbors = [(y, x+1), (y, x-1), (y-1, x-1), (y-1, x+1), (y+1, x), (y-1, x), (y+1, x-1), (y+1, x+1)]
        return [(y_n, x_n) for y_n, x_n in neighbors if 0 <= y_n < self.height and 0 <= x_n < self.width]

    def set(self, y, x, glow):
        self.map[y][x] = glow


def step(y, x, octomap, flash_coordinates):

    glow = octomap.get(y, x)
    point = (y, x)
    if point in flash_coordinates:
        return octomap, flash_coordinates
    elif int(glow) < 9:
        octomap.set(y, x, glow + 1)
        return octomap, flash_coordinates
    elif glow == 9:
        # flash time
        flash_coordinates.append((y, x))
        octomap.set(y, x, 0)

        # check neighbors for flashes
        neighbors = octomap.get_neighbors(y, x)
        for neighbor in neighbors:
            if neighbor not in flash_coordinates:
                octomap, flash_coordinates = step(neighbor[0], neighbor[1], octomap, flash_coordinates)

    return octomap, flash_coordinates