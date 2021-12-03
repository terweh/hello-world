import os

DAY = 3
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def read_bit_file(bitList, bitLength=0):
    if bitLength == 0:
        with open(bitList) as f:
            first_line = f.readline().strip()
            bitLength = len(first_line)
        bitList = [line.strip() for line in open(bitList)]
    bitCount = {
        "one": [0 for _ in range(bitLength)],
        "zero": [0 for _ in range(bitLength)]}

    for line in bitList:
        for i, bit in enumerate(line):
            if bit == "0":
                bitCount["zero"][i] += 1
            elif bit == "1":
                bitCount["one"][i] += 1
    return bitCount, bitLength, bitList


def main_1(Input):
    bitCount, bitLength, _ = read_bit_file(Input)

    gamma = ""
    epsilon = ""
    for i in range(bitLength):
        gamma += "1" if bitCount["one"][i] > bitCount["zero"][i] else "0"
        epsilon += "1" if bitCount["one"][i] < bitCount["zero"][i] else "0"

    return (int(gamma, 2) * int(epsilon, 2))


def find_Criteria(bitCount, index):
    if bitCount["one"][index] > bitCount["zero"][index]:
        return 1
    elif bitCount["one"][index] == bitCount["zero"][index]:
        return 1
    elif bitCount["one"][index] < bitCount["zero"][index]:
        return 0


def find_Ogr(bitCount, bitLength, bitList, index = 0):
    bitCriteria = find_Criteria(bitCount,index)
    filtered = filter(
        lambda bit: int(bit[index]) == bitCriteria, bitList)
    bitList = list(filtered)

    if len(bitList) > 1:
        bitCount, bitLength, bitList = read_bit_file(bitList, bitLength)
        return find_Ogr(bitCount, bitLength, bitList, index + 1)
    return bitList[0]

def find_CO2(bitCount, bitLength, bitList, index = 0):
    bitCriteria = find_Criteria(bitCount,index)
    filtered = filter(
        lambda bit: int(bit[index]) != bitCriteria, bitList)
    bitList = list(filtered)
    if len(bitList) > 1:
        bitCount, bitLength, bitList = read_bit_file(bitList, bitLength)
        return find_CO2(bitCount, bitLength, bitList, index + 1)
    return bitList[0]


def main_2(input):
    bitCount, bitLength, bitList = read_bit_file(input)

    Ogr = find_Ogr(bitCount, bitLength, bitList)
    CO2 = find_CO2(bitCount, bitLength, bitList)
    
    return (int(Ogr, 2) * int(CO2, 2))
