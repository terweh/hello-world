import os
from collections import Counter

DAY = 14
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def from_file(input):
    pairs = []
    insertions = {}
    with open(input) as file:
        instructions = False
        for line in file:
            line = line.strip()
            if instructions:
                insertion = line.split(" -> ")
                insertions.update({insertion[0]: insertion[1]})
            elif line == "":
                instructions = True
            else:
                for i, letter in enumerate(line):
                    if i+1 < len(line):
                        pairs.append(letter+line[i+1])
                last = line[-1]
    return dict(Counter(pairs)), insertions, last


def apply_insertions(pairs, insertions):
    new_pairs = {}
    for pair in pairs:
        try:
            new_pairs[pair[0] + insertions[pair]] += pairs[pair]
        except Exception:
            new_pairs.update({pair[0] + insertions[pair]: pairs[pair]})
        try:
            new_pairs[insertions[pair] + pair[1]] += pairs[pair]
        except Exception:
            new_pairs.update({insertions[pair] + pair[1]: pairs[pair]})

    return new_pairs


def make_x_steps(pairs, insertions, last, x):
    for _ in range(x):
        pairs = apply_insertions(pairs, insertions)

    counter = {}
    for pair in pairs:
        try:
            counter[pair[0]] += pairs[pair]
        except Exception:
            counter.update({pair[0]: pairs[pair]})
    counter[last] += 1

    mx = max(counter, key=counter.get)
    mn = min(counter, key=counter.get)
    return counter[mx] - counter[mn]


def main_1(input):
    pairs, insertions, last = from_file(input)
    return make_x_steps(pairs, insertions, last, 10)


def main_2(input):
    pairs, insertions, last = from_file(input)
    return make_x_steps(pairs, insertions, last, 40)
