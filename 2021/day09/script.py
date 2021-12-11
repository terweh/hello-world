import os

DAY = 9
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def from_file(input):
    with open(input) as file:
        matrix = []
        for line in file:
            matrix.append(list(map(int, line.strip())))

    lowpoints = []
    lowpositions = []
    for line_pos, line in enumerate(matrix):
        for column_pos, height in enumerate(line):
            if check_neighbors(matrix, line_pos, column_pos):
                lowpoints.append(height)
                lowpositions.append([line_pos, column_pos])

    return matrix, lowpoints, lowpositions


def check_neighbors(matrix, line_pos, column_pos):
    center = matrix[line_pos][column_pos]
    if line_pos > 0:
        if matrix[line_pos-1][column_pos] <= center:
            return False
    if column_pos > 0:
        if matrix[line_pos][column_pos-1] <= center:
            return False
    if line_pos < len(matrix)-1:
        if matrix[line_pos+1][column_pos] <= center:
            return False
    if column_pos < len(matrix[line_pos])-1:
        if matrix[line_pos][column_pos+1] <= center:
            return False
    return True


def continue_expansion(matrix, p, visited):
    if matrix[p[0]][p[1]] < 9:
        if ",".join(map(str, p)) not in visited:
            return expand_basin(matrix, p, visited)


def expand_basin(matrix, point, visited):
    visited.add(",".join(map(str, point)))
    if point[0] > 0:
        continue_expansion(
            matrix, [point[0]-1, point[1]], visited)
    if point[1] > 0:
        continue_expansion(
            matrix, [point[0], point[1]-1], visited)
    if point[0] < len(matrix)-1:
        continue_expansion(
            matrix, [point[0]+1, point[1]], visited)
    if point[1] < len(matrix[point[0]])-1:
        continue_expansion(
            matrix, [point[0], point[1]+1], visited)
    return visited


def main_1(input):
    _, lowpoints, _ = from_file(input)

    return sum(lowpoints) + len(lowpoints)


def main_2(input):
    matrix, _, lowpositions = from_file(input)

    basins = []
    for position in lowpositions:
        basins.append(expand_basin(matrix, position, set([])))

    top_3 = sorted([len(x) for x in basins], reverse=True)[:3]

    return top_3[0] * top_3[1] * top_3[2]
