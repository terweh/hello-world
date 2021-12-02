import os

DAY = 2
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def main_1(input):

    dist = 0
    dept = 0
    for line in open(input):
        line = line.strip("\n")
        dir, speed = line.split(" ")
        if dir == "forward":
            dist += int(speed)
        elif dir == "down":
            dept += int(speed)
        elif dir == "up":
            dept -= int(speed)
    return dist * dept


def main_2(input):
    dist = 0
    dept = 0
    aim = 0
    for line in open(input):
        line = line.strip()
        dir, speed = line.split()
        if dir == "forward":
            dist += int(speed)
            dept += aim * int(speed)
        elif dir == "down":
            aim += int(speed)
        elif dir == "up":
            aim -= int(speed)
    return dist * dept
