import os

DAY = 10
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")

legal_pairs = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("<", ">")
]

fees = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

costs = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def parse_line(line):
    collector = []
    for element in line:
        if element in ("(", "{", "[", "<"):
            collector.append(element)
        else:
            opened = collector.pop()
            if (opened, element) in legal_pairs:
                pass
            else:
                return fees[element], []
    return 0, collector


def close_collector(collector):
    score = 0
    while len(collector) > 0:
        to_close = collector.pop()
        score *= 5
        score += costs[to_close]
    return score


def main_1(input):
    score = 0
    with open(input) as file:
        for line in file:
            fee, _ = parse_line(line.strip())
            score += fee
    return score


def main_2(input):
    scores = []
    with open(input) as file:
        for line in file:
            fee, collector = parse_line(line.strip())
            if fee == 0:
                scores.append(close_collector(collector))
    scores = sorted(scores)
    return scores[int(len(scores)/2)]
