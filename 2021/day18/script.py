import os
from ast import literal_eval as parse
DAY = 0  # TODO
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def validate(number, level=1):
    if level == 5:
        return number
    for n in number:
        if isinstance(n, list):
            n1, n2 = validate(n, level=level+1)
        else:
            return n



def addition(number_1, number_2):
    number = [number_1, number_2]
    number = validate(number)
    return(number)


def main_1(input):
    sum = ""
    with open(input) as file:
        for line in file:
            line = parse(line.strip())
            if sum == "":
                sum = line
                continue
            sum = addition(sum, line)
    print(sum)
    return 0


def main_2(input):
    # TODO
    with open(input) as file:
        for line in file:
            pass  # TODO
    return 0


print(main_1(TESTING))
