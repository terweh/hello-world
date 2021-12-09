import os

DAY = 8
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def main_1(input):
    count = 0
    with open(input) as file:
        for line in file:
            _, valve_digits = parse_line(line)
            for digit in valve_digits:
                if len(digit) in [2, 3, 4, 7]:
                    count += 1
    return count


def parse_line(line):
    line = line.strip().split("|")
    return(
        list(map(sorted,  line[0].split())),
        list(map(sorted, line[1].split())))


def first_mapping(numbers):
    """maps the unique letters (1, 7, 4, 8) and returns the rest as groups"""
    mapping = {}
    sixs = []
    fives = []
    for digit in numbers:
        if len(digit) == 2:
            mapping.update({"1": digit})
        elif len(digit) == 3:
            mapping.update({"7": digit})
        elif len(digit) == 4:
            mapping.update({"4": digit})
        elif len(digit) == 5:
            fives.append(digit)
        elif len(digit) == 6:
            sixs.append(digit)
        elif len(digit) == 7:
            mapping.update({"8": digit})
    return mapping, fives, sixs


def map_sixs(mapping, sixs):
    """1 fits in 0 and 9, but only 4 in 9 and others must be 6"""
    for digit in sixs:
        if all(d in digit for d in mapping["1"]):
            if all(d in digit for d in mapping["4"]):
                mapping.update({"9": digit})
            else:
                mapping.update({"0": digit})
        else:
            mapping.update({"6": digit})
    return mapping


def map_fives(mapping, fives):
    """5 and 3 fit in 9, but only 5 in 6 and others must be 2"""
    for digit in fives:
        if all(d in mapping["9"] for d in digit):
            if all(d in mapping["6"] for d in digit):
                mapping.update({"5": digit})
            else:
                mapping.update({"3": digit})
        else:
            mapping.update({"2": digit})
    return mapping


def main_2(input):
    count = 0
    with open(input) as file:
        for line in file:
            numbers, valve_digits = parse_line(line)

            mapping, fives, sixs = first_mapping(numbers)

            mapping = map_sixs(mapping, sixs)
            mapping = map_fives(mapping, fives)

            for i, digit in enumerate(valve_digits):
                valve_digits[i] = list(mapping.keys())[
                    list(mapping.values()).index(digit)]
            count += int("".join(valve_digits))
    return count
