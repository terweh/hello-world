import os
from collections import Counter

DAY = 3
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def read_bit_file(input):
    """
    read a file and store it's values in a list.
    returns a list of binaries (as strings) and the bit length.
    """
    with open(input) as f:
        bit_list = [line.strip() for line in f]
    return bit_list, len(bit_list[0])


def get_bit_counts(bit_list, bit_length):
    """
    returns the counts for ones and zeros in a list of binaries per position.
    """
    bit_count = {
        "one": [0] * bit_length,
        "zero": [0] * bit_length}

    for i in range(bit_length):
        counts = Counter(bit[i] for bit in bit_list)
        bit_count["one"][i] = counts["1"]
        bit_count["zero"][i] = counts["0"]

    return bit_count


def find_criteria(bit_count, index, invert=False):
    """
    determine the bit criteria.
    inverted when used for CO2.
    """
    if bit_count["one"][index] >= bit_count["zero"][index]:
        return "0" if invert else "1"
    elif bit_count["one"][index] < bit_count["zero"][index]:
        return "1" if invert else "0"


def find_candidates(bit_list, bit_length, bit_count, index=0, invert=False):
    """
    filter the list of binaries according to the determined criteria.
    (or invertion thereof for CO2)
    """
    bit_criteria = find_criteria(bit_count, index, invert=invert)

    # filter list by criteria for byte at index
    filtered = filter(
        lambda bit: bit[index] == bit_criteria, bit_list)
    bit_list = list(filtered)

    # if there are still more than 1 continue until one is left
    if len(bit_list) > 1:
        return find_candidates(
            bit_list, bit_length, get_bit_counts(bit_list, bit_length),
            index + 1, invert=invert)

    return bit_list[0]


def main_1(input):
    bit_list, bit_length = read_bit_file(input)
    bit_count = get_bit_counts(bit_list, bit_length)

    gamma = "".join(
        find_criteria(bit_count, i)
        for i in range(bit_length))
    epsilon = "".join(
        find_criteria(bit_count, i, invert=True)
        for i in range(bit_length))

    # multiply the intigers derrived from the binaries
    return (int(gamma, 2) * int(epsilon, 2))


def main_2(input):
    bit_list, bit_length = read_bit_file(input)
    bit_count = get_bit_counts(bit_list, bit_length)

    # find the correct binary by applying the criteria rules
    o_gr = find_candidates(bit_list, bit_length, bit_count)
    co_2 = find_candidates(bit_list, bit_length, bit_count, invert=True)

    # multiply the intigers derrived from the binaries
    return (int(o_gr, 2) * int(co_2, 2))
