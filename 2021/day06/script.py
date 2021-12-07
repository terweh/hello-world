import os

DAY = 6
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def pass_days(old_population, days):
    population = {
        0: old_population[1],
        1: old_population[2],
        2: old_population[3],
        3: old_population[4],
        4: old_population[5],
        5: old_population[6],
        6: old_population[7] + old_population[0],
        7: old_population[8],
        8: old_population[0]}
    days -= 1
    if days == 0:
        return population
    else:
        return pass_days(population, days)


def from_file(input):
    population = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    with open(input) as file:
        for fish in file.readline().strip().split(","):
            population[int(fish)] += 1
    return population


def main_1(input):
    population = from_file(input)
    population = pass_days(population, 80)
    return sum(population[x] for x in population)


def main_2(input):
    population = from_file(input)
    population = pass_days(population, 256)
    return sum(population[x] for x in population)
