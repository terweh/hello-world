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


def main_1(input):
    vents = []
    with open(input) as file:
        for line in file:
            line = line.strip()
            a, _, b = line.split()
            a = [int(i) for i in a.split(",")]
            b = [int(i) for i in b.split(",")]
            if a[0] == b[0]:
                step = 1 if a[1] < b[1] else -1
                for n in range(a[1], b[1]+step, step):
                    vents.append(f"{a[0]},{n}")
            elif a[1] == b[1]:
                step = 1 if a[0] < b[0] else -1
                for n in range(a[0], b[0]+step, step):
                    vents.append(f"{n},{a[1]}")

    return counter(vents)


def main_2(input):
    vents = []
    with open(input) as file:
        for line in file:
            line = line.strip()
            a, _, b = line.split()
            a = [int(i) for i in a.split(",")]
            b = [int(i) for i in b.split(",")]
            if a[0] == b[0]:
                step = 1 if a[1] < b[1] else -1
                for n in range(a[1], b[1]+step, step):
                    vents.append(f"{a[0]},{n}")
            elif a[1] == b[1]:
                step = 1 if a[0] < b[0] else -1
                for n in range(a[0], b[0]+step, step):
                    vents.append(f"{n},{a[1]}")
            else:
                step_0 = 1 if a[0] < b[0] else -1
                step_1 = 1 if a[1] < b[1] else -1
                for x, y in zip(
                        range(a[0], b[0]+step_0, step_0),
                        range(a[1], b[1]+step_1, step_1)):
                    vents.append(f"{x},{y}")
    return counter(vents)


print(main_2(INPUT))
