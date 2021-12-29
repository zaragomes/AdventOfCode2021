from day11 import OctoMap, step

octomap = OctoMap()
flashes = 0
steps = 500
for i in range(0, steps):
    flash_coordinates = []
    for y in range(0, octomap.height):
        for x in range(0, octomap.width):
            octomap, flash_coordinates = step(y, x, octomap, flash_coordinates)
    if len(flash_coordinates) == octomap.height * octomap.width:
        print(i + 1)
        break


