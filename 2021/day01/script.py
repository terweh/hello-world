import os

DAY = 1
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def main_1(input):
    previous = 0
    counter = 0
    for line in open(input):
        number = int(line.strip())
        if previous == 0:
            previous = number
            continue
        if number > previous:
            counter += 1
            previous = number
        else:
            previous = number
    return counter


def main_2(input):
    pre1 = 0
    pre2 = 0
    previous = 0
    counter = 0

    for line in open(input):
        number = int(line.strip())
        sum = pre1 + pre2 + number

        if pre1 == 0 or pre2 == 0:
            pass
        elif previous == 0 and (pre1 > 0 and pre2 > 0):
            previous = sum
        elif sum > previous:
            counter += 1
            previous = sum
        elif previous > 0:
            previous = sum
        pre2 = pre1
        pre1 = number

    return counter
