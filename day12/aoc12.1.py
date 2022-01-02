from day12 import CaveMap

cavemap = CaveMap()
paths = cavemap.calculate_paths(cavemap.START, allow_double_visits=False)
print(len(paths))