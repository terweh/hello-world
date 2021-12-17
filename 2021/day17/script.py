import os

DAY = 17
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def run(spd, area):
    pos = {"x": 0, "y": 0}
    ymax = 0
    return step(spd, pos, area, ymax)


def step(spd, pos, area, ymax):
    pos["x"] += spd["x"]
    pos["y"] += spd["y"]
    ymax = pos["y"] if ymax < pos["y"] else ymax
    spd["x"] += -1 if spd["x"] != 0 else 0
    spd["y"] += -1
    if pos["y"] < area["y"][-1] or pos["x"] > area["x"][-1]:
        return False, ymax
    elif pos["x"] >= area["x"][0] and pos["y"] <= area["y"][0]:
        return True, ymax
    return step(spd, pos, area, ymax)


def mark_area(input):
    with open(input) as file:
        line = file.readline().strip()
        line = line.split(" ")
        x = line[2][2:].strip(",").split("..")
        y = line[3][2:].split("..")

    return {
        "x": list(range(int(x[0]), int(x[1])+1)),
        "y": list(range(int(y[1]), int(y[0])-1, -1))}


def reach_area(area):
    min_x = [
        x for x in range(area["x"][0])
        if (x * (x + 1) / 2) >= area["x"][0]][0]
    max_y = abs(area["y"][-1])
    return min_x, area["x"][-1]+1, area["y"][-1]-1, max_y


def main_1(input):
    area = mark_area(input)
    min_x, max_x, min_y, max_y = reach_area(area)

    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            spd = {"x": x, "y": y}
            check, ymax = run(spd, area)
            if check:
                return ymax


def main_2(input):
    area = mark_area(input)
    min_x, max_x, min_y, max_y = reach_area(area)
    count = 0
    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            spd = {"x": x, "y": y}
            check, _ = run(spd, area)
            if check:
                count += 1
    return count
