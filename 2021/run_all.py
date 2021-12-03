from argparse import ArgumentParser


def run(number):
    try:
        day = getattr(
            __import__(f"day{number}", fromlist=["script"]), "script")
    except ModuleNotFoundError as e:
        print(f"Day {number} in not yet available\nError: {e}\n")
        return
    print("Day {}".format(day.DAY))
    print("{}.1:    {}".format(day.DAY, day.main_1(day.INPUT)))
    print("{}.2:    {}".format(day.DAY, day.main_2(day.INPUT)))
    print()


if __name__ == '__main__':
    parser = ArgumentParser(description='run advent of code for specific days')
    parser.add_argument(
        '--days', '-d', type=int, nargs='+', help='list of days to run')

    args = parser.parse_args()

    if args.days:
        for day in args.days:
            run(f"{day:02}")
    else:
        for day in [1, 2]:
            run(f"{day:02}")
