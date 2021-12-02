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


# class Test_Day3(Test_Day0):
#     import day03.script as day
#     result_1 = 0  # TODO
#     result_2 = 0  # TODO
