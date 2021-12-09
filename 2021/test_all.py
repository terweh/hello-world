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


class Test_Day1(Test_Day0):
    import day01.script as day
    expt_1 = 7
    expt_2 = 5


class Test_Day2(Test_Day0):
    import day02.script as day
    expt_1 = 150
    expt_2 = 900


class Test_Day3(Test_Day0):
    import day03.script as day
    expt_1 = 198
    expt_2 = 230


class Test_Day4(Test_Day0):
    import day04.script as day
    expt_1 = 4512
    expt_2 = 1924


class Test_Day5(Test_Day0):
    import day05.script as day
    expt_1 = 5
    expt_2 = 12


class Test_Day6(Test_Day0):
    import day06.script as day
    expt_1 = 5934
    expt_2 = 26984457539


class Test_Day7(Test_Day0):
    import day07.script as day
    expt_1 = 37
    expt_2 = 162


class Test_Day8(Test_Day0):
    import day08.script as day
    expt_1 = 26
    expt_2 = 61229


class Test_Day9(Test_Day0):
    import day09.script as day
    expt_1 = 15
    expt_2 = 1134


# class Test_Day3(Test_Day0):
#     import day03.script as day
#     expt_1 = 0  # TODO
#     expt_2 = 0  # TODO
