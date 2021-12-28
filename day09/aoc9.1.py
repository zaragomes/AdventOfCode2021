from day09 import Heightmap


def calculate_risk():
    risk_score = 0
    heightmap = Heightmap()
    for y in range(0, heightmap.height):
        for x in range(0, heightmap.width):
            neighbors = heightmap.get_neighbors(y, x)
            if heightmap.map[y][x] < min(heightmap.get(neighbor[0], neighbor[1]) for neighbor in neighbors):
                risk_score = risk_score + heightmap.get(y, x) + 1
    return risk_score


print(calculate_risk())
