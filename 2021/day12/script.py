import os

DAY = 12
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")
T1 = os.path.join(PATH, "test_1.txt")
T2 = os.path.join(PATH, "test_2.txt")


def go_from(origin, paths, visited):
    count = 0
    new_visited = list(visited)
    new_visited.append(origin)
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
            )
    ]
    for path in possible_ways:
        count += go_from(path[1], paths, new_visited)
    return count


def from_file(input):
    paths = []
    with open(input) as file:
        for line in file:
            line = line.strip().split("-")
            paths.extend([[line[0], line[1]], [line[1], line[0]]])
    return paths


def main_1(input):
    paths = from_file(input)
    return go_from('start', paths, [])


def main_2(input):
    paths = from_file(input)
    return 0

print(main_2(T1))
