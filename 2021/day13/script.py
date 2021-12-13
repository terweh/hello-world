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
                folds.append((1 if fold[0][-1:] == 'y' else 0, int(fold[1])))
            elif line == "":
                instructions = True
            else:
                point = line.split(",")
                points.add((int(point[0]), int(point[1])))
    return points, folds


def fold_over(fold, points):
    dim, pos = fold
    new_points = set()
    for point in points:
        if point[dim] > pos:
            new_point = list(point)
            new_point[dim] = pos - (point[dim] - pos)
            new_points.add(tuple(new_point))
        else:
            new_points.add(point)
    return new_points


def printer(points):
    x_dim = max(x[0] for x in points)+1
    y_dim = max(y[1] for y in points)+1
    result = "\n"
    for y in range(y_dim):
        for x in range(x_dim):
            result += "█" if (x, y) in points else " "
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
