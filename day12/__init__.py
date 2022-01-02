from typing import List , Optional, Tuple
from collections import Counter


def get_lines_from_input():
    with open("input.txt") as file:
        return [line.strip() for line in file]


class CaveMap:
    START = "start"
    END = "end"

    def __init__(self):
        self.map = {}
        for line in get_lines_from_input():
            x1, x2 = line.split("-")
            self.map.setdefault(x1, set()).add(x2)
            self.map.setdefault(x2, set()).add(x1)

    @staticmethod
    def is_cave_small(self, cave: str):
        return cave.islower()

    @staticmethod
    def is_cave_large(self, cave: str):
        return cave.isupper()

    def is_cave_eligible(self, cave:str, start, current_path, allow_double_visits):
        eligible = False
        lower_caves = [cave for cave in current_path if cave.islower()]
        caves_counter = Counter(lower_caves)
        if self.is_cave_small(self, cave):
            if not allow_double_visits and cave not in current_path:
                return True
            if allow_double_visits:
                if (cave == "start" or cave == "end") and cave in current_path:
                    return False
                if caves_counter.most_common()[0][1] == 1:
                    return True
                if cave not in current_path:
                    return True

        if self.is_cave_large(self, cave):
            return True
        # if (start + ", " + cave) in ", ".join(current_path):
        #     return False
        if cave == self.END:
            return True
        return False

    def calculate_paths(self,
                        start: str,
                        current_path: Optional[Tuple[str]] = None,
                        passage_paths: Optional[List[Tuple[str]]] = None,
                        allow_double_visits=True):
        if passage_paths is None:
            passage_paths = []

        if current_path is None:
            current_path = [start]

        for current_node in self.map[start]:
            if self.is_cave_eligible(current_node, start, current_path, allow_double_visits):
                new_path = current_path + [current_node]
                if current_node == self.END:
                    passage_paths.append(new_path)
                else:
                    passage_paths = self.calculate_paths(current_node, new_path, passage_paths, allow_double_visits)

        return passage_paths





