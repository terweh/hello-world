import day01.script
import day02.script



def run(module):
    print("Day {}".format(module.DAY))
    print("{}.1:    {}".format(module.DAY, module.main_1(module.INPUT)))
    print("{}.2:    {}".format(module.DAY, module.main_2(module.INPUT)))
    print()


run(day01.script)
run(day02.script)
