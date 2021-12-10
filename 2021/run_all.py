from argparse import ArgumentParser
import timeit


def run(number, timer):
    try:
        day = getattr(
            __import__(f"day{number}", fromlist=["script"]), "script")
    except ModuleNotFoundError as e:
        print(f"Day {number} in not yet available\nError: {e}\n")
        return
    print("Day {}".format(day.DAY))
    print("{}.1:    {}".format(day.DAY, day.main_1(day.INPUT)))
    if timer:
        time = timeit.timeit(
            stmt='day.main_1(day.TESTING)',
            setup=f'from day{number} import script as day',
            number=10000)
        print(f"\tTIME: {time}")
    print("{}.2:    {}".format(day.DAY, day.main_2(day.INPUT)))
    if timer:
        time = timeit.timeit(
            stmt='day.main_2(day.TESTING)',
            setup=f'from day{number} import script as day',
            number=100)
        print(f"\tTIME: {time}")
    print()


if __name__ == '__main__':
    parser = ArgumentParser(description='run advent of code for specific days')
    parser.add_argument(
        '--days', '-d', type=int, nargs='+', help='list of days to run')
    parser.add_argument(
        '--timer', '-t', action='store_true', help='run timer for each day')

    args = parser.parse_args()

    if args.days:
        for day in args.days:
            run(f"{day:02}", args.timer)
    else:
        for day in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            run(f"{day:02}", args.timer)
