import os

DAY = 16
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def split(x, y):
    return [x[i:i+y] for i in range(0, len(x), y)]


def hex2bin(hex):
    b = ''
    for d in hex:
        b += f'{int(d, 16):04b}'
    return b


def main_1(input):
    a = [
        # "D2FE28",
        # "38006F45291200",
        # "EE00D40C823060",
        "8A004A801A8002F478",
        "620080001611562C8802118E34",
        "C0015000016115A2E0802F182340",
        "A0016C880162017C3686B18A3D4780"
    ]

    for x in a:
        bit_string = hex2bin(x)
        return process_hex(bit_string)
        exit()


def process_hex(bit_string):
    version = int(bit_string[:3], 2)
    s_type = int(bit_string[3:6], 2)

    # print(bit_string)
    if s_type == 4:
        rest = bit_string[6:]
        # print(f"version: {version}")
        # print(f"type: {s_type}")
        # print(bit_string[:3], bit_string[3:6], rest)
        # print(bit_string, version, s_type, literal(rest))
        return version
    else:
        l_type = bit_string[6:7]
        # print(f"version: {version}")
        # print(f"type: {s_type}")
        # print(f"len_type: {l_type}")

        if l_type == "0":
            subs_len = int(bit_string[7:7+15], 2)
            rest = bit_string[7+15:]
            # print(f"subs_len: {subs_len}")
            # print(bit_string[:3], bit_string[3:6], bit_string[7:7+15], rest)
            # print(f"take 15 to determine length: {subs_len}")
            return version + sub_by_len(subs_len, rest)
        else:
            subs_n = int(bit_string[7:7+11], 2)
            rest = bit_string[7+11:]
            # print(f"subs_n: {subs_n}")
            # print(bit_string[:3], bit_string[3:6], bit_string[7:7+11], rest)
            # print(f"take 11 to determine number: {subs_n}")
            return version + sub_by_n(subs_n, rest)


def sub_by_len(subs_len, rest):
    full = [rest[:11], rest[11:subs_len]]
    if full[1]:
        return sum([process_hex(x) for x in full])
    else:
        return process_hex(full[0])


def sub_by_n(subs_n, rest):
    full = split(rest, 11)
    sub_packs = []
    for i, x in enumerate(full):
        if i < subs_n-1:
            sub_packs.append(x)
    sub_packs.append("".join(full[subs_n-1:]))
    return sum([process_hex(x) for x in sub_packs])


def literal(rest):
    bits = split(rest, 5)
    lit = ""
    for bit in bits:
        lit += bit[1:]
        if bit[0] == "0":
            break
    return int(lit, 2)


def main_2(input):
    # TODO
    with open(input) as file:
        for line in file:
            pass  # TODO
    return 0


print(main_1(TESTING))
