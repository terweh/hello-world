import pytest
import os

PATH = os.path.dirname(os.path.realpath(__file__))
__all__ = [pytest]


def test_alive():
    assert True


class Test_Day0():
    import day00.script as day
    expt_1 = 0
    expt_2 = 0

    def test_1(self):
        a = self.day.main_1(self.day.TESTING)
        print(f"a: {a}, self.expt_1: {self.expt_1}")
        assert a == self.expt_1

    def test_2(self):
        a = self.day.main_2(self.day.TESTING)
        assert a == self.expt_2


class Test_Day01(Test_Day0):
    import day01.script as day
    expt_1 = 7
    expt_2 = 5


class Test_Day02(Test_Day0):
    import day02.script as day
    expt_1 = 150
    expt_2 = 900


class Test_Day03(Test_Day0):
    import day03.script as day
    expt_1 = 198
    expt_2 = 230


class Test_Day04(Test_Day0):
    import day04.script as day
    expt_1 = 4512
    expt_2 = 1924


class Test_Day05(Test_Day0):
    import day05.script as day
    expt_1 = 5
    expt_2 = 12


class Test_Day06(Test_Day0):
    import day06.script as day
    expt_1 = 5934
    expt_2 = 26984457539


class Test_Day07(Test_Day0):
    import day07.script as day
    expt_1 = 37
    expt_2 = 162


class Test_Day08(Test_Day0):
    import day08.script as day
    expt_1 = 26
    expt_2 = 61229


class Test_Day09(Test_Day0):
    import day09.script as day
    expt_1 = 15
    expt_2 = 1134


class Test_Day10(Test_Day0):
    import day10.script as day
    expt_1 = 26397
    expt_2 = 288957


class Test_Day11(Test_Day0):
    import day11.script as day
    expt_1 = 1656
    expt_2 = 195


class Test_Day12(Test_Day0):
    import day12.script as day
    expt_1 = 226
    expt_2 = 3509


class Test_Day13(Test_Day0):
    import day13.script as day
    expt_1 = 17
    expt_2 = "\n█████\n█   █\n█   █\n█   █\n█████\n"


class Test_Day14(Test_Day0):
    import day14.script as day
    expt_1 = 1588
    expt_2 = 2188189693529


class Test_Day15(Test_Day0):
    import day15.script as day
    expt_1 = 40
    expt_2 = 315


# class Test_Day3(Test_Day0):
#     import day03.script as day
#     expt_1 = 0  # TODO
#     expt_2 = 0  # TODO
