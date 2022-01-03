from day13 import Paper

paper = Paper()

axis, unit = paper.instr[0].split("=")
paper.fold_along_axis(axis, int(unit))
print(len(paper.points_counter))
