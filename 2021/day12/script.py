import os

DAY = 12
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")
T1 = os.path.join(PATH, "test_1.txt")
T2 = os.path.join(PATH, "test_2.txt")


def go_from(origin, paths, visited, extra_visit=""):
    count = 0
    new_visited = list(visited)
    new_visited.append(origin)
    if new_visited.count(extra_visit) > 1:
        extra_visit = ""

    if origin == 'end':
        # print(",".join(new_visited))
        return 1

    possible_ways = [
        path
        for path in paths
        if path[0] == origin
        if (
            path[1] not in visited
            or path[1].isupper()
            or path[1] == extra_visit
            )
    ]

    for path in possible_ways:
        count += go_from(path[1], paths, new_visited, extra_visit)
    return count


def from_file(input):
    paths = []
    small_caves = []
    with open(input) as file:
        for line in file:
            line = line.strip().split("-")
            paths.extend([[line[0], line[1]], [line[1], line[0]]])
            for cave in line:
                if (
                        cave.islower()
                        and cave not in small_caves
                        and cave not in ['start', 'end']):
                    small_caves.append(cave)
    return paths, small_caves


def main_1(input):
    paths, _ = from_file(input)
    return go_from('start', paths, [])


def main_2(input):
    paths, small_caves = from_file(input)
    default = go_from('start', paths, [])
    count = default
    print(small_caves)
    for cave in small_caves:
        count += go_from('start', paths, [], cave) - default
    return count


print(main_1(TESTING))
print(main_2(INPUT))
