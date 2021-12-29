from day11 import OctoMap, step


octomap = OctoMap()
flashes = 0
steps = 100
for _ in range(0, steps):
    flash_coordinates = []
    for y in range(0, octomap.height):
        for x in range(0, octomap.width):
            octomap, flash_coordinates = step(y, x, octomap, flash_coordinates)
    flashes += len(flash_coordinates)

print(flashes)

