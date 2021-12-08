import os

DAY = 4
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


class Bingo():
    def __init__(self):
        self.lines = []
        self.columns = []
        self.changed = False

    def add_line(self, array):
        self.lines.append(array)
        for i, number in enumerate(array):
            try:
                self.columns[i].append(number)
            except Exception:
                self.columns.append([number])

    def print(self):
        print(self.lines)
        print(self.columns)

    def update(self, number):
        self.changed = False
        for i in self.lines:
            try:
                i.remove(number)
                self.changed = True
            except Exception:
                pass
        for i in self.columns:
            try:
                i.remove(number)
                self.changed = True
            except Exception:
                pass

    def check(self):
        if self.changed:
            if [] in self.lines:
                return self.last_numbers()
            if [] in self.columns:
                return self.last_numbers()

    def last_numbers(self):
        return [num for line in self.lines for num in line]


def generate_bingo(input):
    first = None
    index = -1
    bingos = []
    with open(input) as file:
        for line in file:
            line = line.strip("\n")
            if not line:
                bingos.append(Bingo())
                index += 1
                continue
            if first:
                bingos[index].add_line([int(num) for num in line.split()])
            else:
                first = [int(num) for num in line.split(",")]
    for b in bingos:
        if len(b.lines) != 5 or len(b.columns) != 5:
            print("ERROR: recheck input data. there are empy bingos")
            # too many empty lines ?
            exit(os.error)
    return (bingos, first)


def run_bingo(bingos, numbers):
    for n in numbers:
        for b in bingos:
            b.update(n)
            rest = b.check()
            if rest:
                return sum(rest) * n

    return os.error


def run_to_last_bingo(bingos, numbers):
    for n in numbers:
        for b in bingos:
            b.update(n)
        for b in bingos:
            rest = b.check()
            if rest:
                bingos.remove(b)
            if len(bingos) == 0:
                return sum(rest) * n

    return os.error


def main_1(input):
    bingos, numbers = generate_bingo(input)
    return run_bingo(bingos, numbers)


def main_2(input):
    bingos, numbers = generate_bingo(input)
    return run_to_last_bingo(bingos, numbers)
