import os
# from collections import defaultdict

DAY = 15
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def from_file(input):
    matrix = []
    with open(input) as file:
        for line in file:
            line = line.strip()
            matrix.append([int(risk) for risk in line])
    return matrix


def from_file_2(input):
    matrix = []
    matrix_draft = []
    with open(input) as file:
        for line in file:
            line = line.strip()
            line_draft = []
            for i in range(5):
                line_draft.extend([int(risk)+i for risk in line])
            matrix_draft.append(line_draft)
    for i in range(5):
        matrix.extend([
            [((risk-1+i) % 9)+1 for risk in line] for line in matrix_draft])
    return matrix


def first_risks(matrix, risks):
    for y, _ in enumerate(risks):
        for x, risk in enumerate(_):
            if x > 0:
                if y > 0:
                    low = min([risks[y-1][x], risks[y][x-1]])
                else:
                    low = risks[y][x-1]
            elif y > 0:
                low = risks[y-1][x]
            else:
                low = -matrix[y][x]
            risks[y][x] = low + matrix[y][x]
    return matrix, risks


def adjust_risks(matrix, risks):
    count = []
    for y, line in enumerate(risks):
        for x, risk in enumerate(line):
            count.extend(adjust_single(risks, matrix, x, y))
    if count:
        adjust_area(matrix, risks, count)
    else:
        return


def adjust_single(risks, matrix, x, y):
    current = risks[y][x]
    weight = matrix[y][x]
    neighbors = [current - weight]
    if x+1 < len(risks[0]):
        neighbors.append(risks[y][x+1])
    if y+1 < len(risks):
        neighbors.append(risks[y+1][x])
    if x > 0:
        neighbors.append(risks[y][x-1])
    if y > 0:
        neighbors.append(risks[y-1][x])
    low = min(neighbors)
    if current > low + weight:
        risks[y][x] = low + weight
        return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
    return []


def adjust_area(matrix, risks, area):
    count = []
    for x, y in area:
        if(x >= len(risks[0]) or y >= len(risks) or x < 0 or y < 0):
            continue
        count.extend(adjust_single(risks, matrix, x, y))
    if count:
        adjust_area(matrix, risks, count)
    else:
        return


def traverse(matrix):
    risks = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    first_risks(matrix, risks)
    adjust_risks(matrix, risks)
    return risks[-1][-1]


"""
def traverse(matrix):
    visited = defaultdict()
    risks = defaultdict(int)
    risks[(0, 0)] = 0
    visited[(0, 0)] = "(0, 0)"

    risk = 0
    loc = (0, 0)
    count = 0
    while risk == 0:
        risk, loc = go_through(matrix, loc[0], loc[1], risks, visited)
        count += 1
        print(f"current count : {count}", end='\r')
    print(count)
    return risk


def go_through(matrix, x, y, risks, visited):
    if x+1 == len(matrix[0]) and y+1 == len(matrix):
        return risks[(x, y)], 0

    if x-1 >= 0:
        current_risk = risks[(x, y)] + matrix[y][x-1]
        if not (x-1, y) in risks or risks[(x-1, y)] > current_risk:
            risks[(x-1, y)] = current_risk
            visited[(x-1, y)] = visited[(x, y)] + f" --> ({x-1}, {y})"
    if y-1 >= 0:
        current_risk = risks[(x, y)] + matrix[y-1][x]
        if not (x, y-1) in risks or risks[(x, y-1)] > current_risk:
            risks[(x, y-1)] = current_risk
            visited[(x, y-1)] = visited[(x, y)] + f" --> ({x}, {y-1})"

    if x+1 < len(matrix[0]):
        current_risk = risks[(x, y)] + matrix[y][x+1]
        if not (x+1, y) in risks or risks[(x+1, y)] > current_risk:
            risks[(x+1, y)] = current_risk
            visited[(x+1, y)] = visited[(x, y)] + f" --> ({x+1}, {y})"
    if y+1 < len(matrix):
        current_risk = risks[(x, y)] + matrix[y+1][x]
        if not (x, y+1) in risks or risks[(x, y+1)] > current_risk:
            risks[(x, y+1)] = current_risk
            visited[(x, y+1)] = visited[(x, y)] + f" --> ({x}, {y+1})"

    del risks[(x, y)]

    low = min(risks, key=risks.get)
    return 0, low  # go_through(matrix, low[0], low[1], risks, visited)
"""


def main_1(input):
    matrix = from_file(input)
    return traverse(matrix)


def main_2(input):
    matrix = from_file_2(input)
    return traverse(matrix)
