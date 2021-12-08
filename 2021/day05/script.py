import os
from collections import Counter

DAY = 5
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def counter(vents):
    count = 0
    counted = Counter(vents)
    for vent in counted:
        if counted[vent] > 1:
            count += 1
    return count

def line2points(line):
    line = line.strip()
    a, _, b = line.split()
    return list(map(int, a.split(","))), list(map(int, b.split(",")))


def vertical_line(a,b):
    step = 1 if a[1] < b[1] else -1
    return [f"{a[0]},{n}" for n in range(a[1], b[1]+step, step)]


def horizontal_line(a,b):
    step = 1 if a[0] < b[0] else -1
    return [f"{n},{a[1]}" for n in range(a[0], b[0]+step, step)]


def diagonal_line(a,b):
    step_0 = 1 if a[0] < b[0] else -1
    step_1 = 1 if a[1] < b[1] else -1
    return [f"{x},{y}" for x, y in zip(
        range(a[0], b[0]+step_0, step_0),
        range(a[1], b[1]+step_1, step_1))]


def main_1(input):
    vents = []
    with open(input) as file:
        for line in file:
            a, b = line2points(line)
            if a[0] == b[0]:  # vertical
                vents.extend(vertical_line(a, b))
            elif a[1] == b[1]:  # horizontal
                vents.extend(horizontal_line(a, b))
    return counter(vents)


def main_2(input):
    vents = []
    with open(input) as file:
        for line in file:
            a, b = line2points(line)
            if a[0] == b[0]:  # vertical
                vents.extend(vertical_line(a, b))
            elif a[1] == b[1]:  # horizontal
                vents.extend(horizontal_line(a, b))
            else:
                vents.extend(diagonal_line(a, b))
    return counter(vents)
