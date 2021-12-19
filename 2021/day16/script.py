import os

DAY = 16
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def product(array):
    outcome = 1
    for number in array:
        outcome *= number
    return outcome


def greater(dublet):
    if dublet[0] > dublet[1]:
        return 1
    return 0


def less(dublet):
    if dublet[0] < dublet[1]:
        return 1
    return 0


def equal(dublet):
    if dublet[0] == dublet[1]:
        return 1
    return 0


types = [
    sum, product, min, max,
    "literal",
    greater, less, equal
]


def split(x, y):
    return [x[i:i+y] for i in range(0, len(x), y)]


def hex2bin(hex):
    b = ''
    for d in hex:
        b += f'{int(d, 16):04b}'
    return b


def main(input):
    version_sum = 0
    number_sum = 0
    with open(input) as file:
        for line in file:
            line = line.strip()
            line = hex2bin(line)
            version, number = process_hex(line)
            version_sum += version
            number_sum += number[0]
    return version_sum, number_sum


def process_hex(bit_string):
    if "1" not in bit_string:
        return 0, []
    version = int(bit_string[:3], 2)
    s_type = int(bit_string[3:6], 2)

    if s_type == 4:
        rest = bit_string[6:]
        number, rest = literal(rest)
        version_sum, outcome = process_hex(rest)
        version_sum += version
        number.extend(outcome)
        return (version_sum, number)
    else:
        l_type = bit_string[6:7]
        if l_type == "0":
            subs_len = int(bit_string[7:7+15], 2)
            rest = bit_string[7+15:]
            version_sum_1, number = process_hex(rest[:subs_len])
            version_sum_2, outcome = process_hex(rest[subs_len:])
            number = [types[s_type](number)]
            version_sum = version_sum_1 + version_sum_2 + version
            number.extend(outcome)
            return (version_sum, number)
        else:
            subs_n = int(bit_string[7:7+11], 2)
            rest = bit_string[7+11:]
            version_sum, outcome = process_hex(rest)
            version_sum += version
            number = [types[s_type](outcome[:subs_n])]
            outcome = outcome[subs_n:]
            number.extend(outcome)
            return (version_sum, number)


def literal(rest):
    bits = split(rest, 5)
    string = ""
    number = ""
    for i, bit in enumerate(bits):
        string += bit[1:]
        if bit[0] == "0":
            number = string
            string = "".join(bits[i+1:])
            break
    return [int(number, 2)], string


def main_1(input):
    version, _ = main(input)
    return version


def main_2(input):
    _, number = main(input)
    return number


print(main_2(INPUT))
