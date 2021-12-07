
import os
From statistics import median, mean

DAY = 7
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")  

def from_file(input)
    with open(input) as file:
        line = file.readline().strip().split(",")
        a = [int(x) for x in line]
    return a


def find_ideal_fuel(a, m, function):
    m_fuel = function(m, a)
    if function(m+1, a) < m_fuel:
        find_ideal_fuel(a, m+1, function)
    elif function(m-1, a) < m_fuel:
        find_ideal_fuel(a, m-1, function)
    else:
        return m_fuel


def fuel_1(m, a):
    summe = 0
    for x in a:
        n = abs(x-i)
        summe += n
    return summe


def fuel_2(m, a):
    summe = 0
    for x in a:
        n = abs(x-i)
        summe += int(((n * n) + n) / 2)
    return summe

def main_1(input):
    a = from_file(input)
    my_median = median(a)
    return find_ideal_fuel(a, median, fuel_1)


def main_2(input):
    a = from_file(input)
    my_mean = mean(a)
    return find_ideal_fuel(a, median, fuel_2)