

def main_1(input):

    dist = 0
    dept = 0
    for line in open(input):
        line = line.strip("\n")
        dir, speed = line.split(" ")
        if dir == "forward":
            dist += int(speed)
        elif dir == "down":
            dept += int(speed)
        elif dir == "up":
            dept -= int(speed)
    print(dist, dept)
    print(dist * dept)


def main_2(input):
    dist = 0
    dept = 0
    aim = 0
    for line in open(input):
        line = line.strip("\n")
        dir, speed = line.split(" ")
        if dir == "forward":
            dist += int(speed)
            dept += aim * int(speed)
        elif dir == "down":
            aim += int(speed)
        elif dir == "up":
            aim -= int(speed)
    print(dist, dept)
    print(dist * dept)

main_1("test_2.txt")
main_1("input_2.txt")

main_2("test_2.txt")
main_2("input_2.txt")
