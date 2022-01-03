from day13 import Paper

paper = Paper()

for command in paper.instr:
    axis, unit = command.split("=")
    paper.fold_along_axis(axis, int(unit))

# create blank canvas and add # for existing dots
art_sheet = [["."] * paper.width for _ in range(paper.height)]
for axes, interval in paper.points_counter.items():
    x, y = axes[0], axes[1]
    art_sheet[y][x] = "#"

for x in range(paper.width):
    line = "".join(art_sheet[x])
    print(line)


