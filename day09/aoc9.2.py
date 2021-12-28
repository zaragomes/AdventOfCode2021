from day09 import Heightmap


def get_basin_height(heightmap, y, x, visited_queue):
    basin_height = 0
    neighbors = [(y, x)]

    while len(neighbors):
        yx = neighbors.pop()
        if yx in visited_queue:
            continue

        height = heightmap.get(yx[0], yx[1])
        visited_queue.append(yx)
        if height < 9:
            basin_height += 1
            new_neighbors = heightmap.get_neighbors(yx[0], yx[1])
            for new_neighbor in new_neighbors:
                if new_neighbor not in neighbors:
                    neighbors.append(new_neighbor)

    return basin_height, visited_queue


def get_all_basins():
    heightmap = Heightmap()
    basins = []
    visited_queue = []
    # get neighbors.
    # if neighbor is 9, stop
    for y in range(0, heightmap.height):
        for x in range(0, heightmap.width):
            height = heightmap.get(y, x)
            curr = (y, x)
            if height < 9 and curr not in visited_queue:
                # get basin
                basin_height, visited_queue = get_basin_height(heightmap, y, x, visited_queue)
                basins.append(basin_height)
    return basins


def calculate_largest_3_basins():
    basins = get_all_basins()
    sorted_basins = sorted(basins)
    return sorted_basins[-3:]


largest_basins = calculate_largest_3_basins()
print(largest_basins[0]*largest_basins[1]*largest_basins[2])

