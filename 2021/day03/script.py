import os

DAY = 3
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def read_bit_file(bitList):
    """
    read a file and store it's values in a list.
    returns a list of binaries (as strings) and the bit length.
    """
    with open(bitList) as f:
        first_line = f.readline().strip()
        bitLength = len(first_line)
    bitList = [line.strip() for line in open(bitList)]
    return bitList, bitLength


def get_bit_counts(bitList, bitLength):
    """
    returns the counts for ones and zeros in a list of binaries per position.
    """
    bitCount = {
        "one": [0 for _ in range(bitLength)],
        "zero": [0 for _ in range(bitLength)]}

    for line in bitList:
        for i, bit in enumerate(line):
            if bit == "0":
                bitCount["zero"][i] += 1
            elif bit == "1":
                bitCount["one"][i] += 1

    return bitCount


def find_Criteria(bitCount, index, invert=False):
    """
    determine the bit criteria.
    inverted when used for CO2.
    """
    if bitCount["one"][index] > bitCount["zero"][index]:
        return "0" if invert else "1"
    elif bitCount["one"][index] == bitCount["zero"][index]:
        return "0" if invert else "1"
    elif bitCount["one"][index] < bitCount["zero"][index]:
        return "1" if invert else "0"


def find_candidates(bitList, bitLength, bitCount, index=0, invert=False):
    """
    filter the list of binaries according to the determined criteria.
    (or invertion thereof for CO2)
    """
    bitCriteria = find_Criteria(bitCount, index, invert=invert)

    # filter list by criteria for byte at index
    filtered = filter(
        lambda bit: bit[index] == bitCriteria, bitList)
    bitList = list(filtered)

    # if there are still more than 1 continue until one is left
    if len(bitList) > 1:
        return find_candidates(
            bitList, bitLength, get_bit_counts(bitList, bitLength),
            index + 1, invert=invert)

    return bitList[0]


def main_1(Input):
    bitList, bitLength = read_bit_file(Input)
    bitCount = get_bit_counts(bitList, bitLength)

    gamma = ""
    epsilon = ""
    for i in range(bitLength):
        # generate binary and its invert position by position
        gamma += find_Criteria(bitCount, i)
        epsilon += find_Criteria(bitCount, i, invert=True)

    # multiply the intigers derrived from the binaries
    return (int(gamma, 2) * int(epsilon, 2))


def main_2(input):
    bitList, bitLength = read_bit_file(input)
    bitCount = get_bit_counts(bitList, bitLength)

    # find the correct binary by applying the criteria rules
    Ogr = find_candidates(bitList, bitLength, bitCount)
    CO2 = find_candidates(bitList, bitLength, bitCount, invert=True)

    # multiply the intigers derrived from the binaries
    return (int(Ogr, 2) * int(CO2, 2))
