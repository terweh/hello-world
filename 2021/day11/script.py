import os
from itertools import count

DAY = 11
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


class Dumbo_Squid():
    def __init__(self, energy, x, y, matrix):
        self.pos = (x, y)
        self.neighbors = self.setup(x, y)
        self.energy = energy
        self.matrix = matrix

    def setup(self, x, y):
        x_min = x
        y_min = y
        x_max = x
        y_max = y
        if x > 0:
            x_min -= 1
        if y > 0:
            y_min -= 1
        if x < 9:
            x_max += 1
        if y < 9:
            y_max += 1

        return [
            (i, j)
            for j in range(y_min, y_max+1)
            for i in range(x_min, x_max+1)
            if i is not x or j is not y
        ]

    def update(self):
        self.energy += 1
        if self.energy > 9:
            self.energy = 0
            return self.neighbors

    def react(self):
        if self.energy != 0:
            return self.update()


def from_file(input):
    with open(input) as file:
        matrix = []
        for j, line in enumerate(file):
            matrix.append([
                Dumbo_Squid(squid, i, j, matrix)
                for i, squid in enumerate(map(int, line.strip()))
            ])
    return matrix


def step(matrix):
    count = 0
    to_react = []
    for i in matrix:
        for j in i:
            n = j.update()
            if n:
                to_react.extend(n)
                count += 1
    if to_react:
        return count + react(matrix, to_react)
    return count


def react(matrix, to_react):
    count = 0
    next_to_react = []
    for j in to_react:
        n = matrix[j[1]][j[0]].react()
        if n:
            next_to_react.extend(n)
            count += 1
    if next_to_react:
        return count + react(matrix, next_to_react)
    return count


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j.energy, end="")
        print()
    print()


def main_1(input):
    matrix = from_file(input)
    count = 0
    for _ in range(100):
        count += step(matrix)

    return count


def main_2(input):
    matrix = from_file(input)
    for i in count():
        if step(matrix) == 100:
            return i+1
