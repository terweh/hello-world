import os

DAY = 13
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def from_file(input):
    points = set()
    folds = []
    with open(input) as file:
        instructions = False
        for line in file:
            line = line.strip()
            if instructions:
                fold = line.split("=")
                folds.append((fold[0][-1:], int(fold[1])))
            elif line == "":
                instructions = True
                continue
            else:
                point = line.split(",")
                points.add((int(point[0]), int(point[1])))
    return points, folds


def fold_over(fold, points):
    if fold[0] == "y":
        return fold_over_dimension(1, fold[1], points)
    else:
        return fold_over_dimension(0, fold[1], points)


def fold_over_dimension(dimension, fold_pos, points):
    remove_points = set()
    add_points = set()
    for point in points:
        if point[dimension] > fold_pos:
            remove_points.add(point)
            new_point = list(point)
            new_point[dimension] = fold_pos - (point[dimension] - fold_pos)
            add_points.add(tuple(new_point))
    points = (points - remove_points) | add_points
    return points


def printer(points):
    x_dim = max(x[0] for x in points)+1
    y_dim = max(y[1] for y in points)+1
    result = "\n"
    for y in range(y_dim):
        for x in range(x_dim):
            if (x, y) in points:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result


def main_1(input):
    points, folds = from_file(input)

    return len(fold_over(folds[0], points))


def main_2(input):
    points, folds = from_file(input)
    for fold in folds:
        points = fold_over(fold, points)

    return printer(points)
