import math
from typing import BinaryIO

HEX_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Package:
    def __init__(self, version, ID, binary):
        self.version = version
        self.id = ID
        self.binary = binary

    def sum_version(self):
        return self.version


class ValuePackage(Package):
    def __init__(self, version, ID, value, binary):
        self.value = value
        super().__init__(version, ID, binary)


class OperatorPackage(Package):
    def __init__(self, version, ID, pkg, binary):
        self.pkg = pkg
        super().__init__(version, ID, binary)

    @property
    def value(self):
        operations = {
            0: sum,
            1: math.prod,
            2: min,
            3: max,
            5: lambda x: self.pkg[0].value > self.pkg[1].value,
            6: lambda x: self.pkg[0].value < self.pkg[1].value,
            7: lambda x: self.pkg[0].value == self.pkg[1].value,
        }
        return operations[self.id]([n.value for n in self.pkg])

    def sum_version(self):
        return sum(p.sum_version() for p in self.pkg) + self.version


def parse_data(puzzle_input: str) -> list[str]:
    binary = "".join(HEX_BIN[c] for c in puzzle_input if c in HEX_BIN)
    _, p = read_next_pkg(binary)
    return p


def read_next_pkg(binary: str):
    if int(binary[3:6], 2) == 4:
        return read_next_value_pgk(binary)
    else:
        return read_next_operator_pkg(binary)


def read_next_value_pgk(binary: str):
    version = int(binary[:3], 2)
    pkg_id = int(binary[3:6], 2)
    value = ""

    for i in range(6, len(binary), 5):
        value += binary[i + 1 : i + 5]
        if binary[i] == "0":
            pkg_bin = binary[: (i + 5)]
            pkg = ValuePackage(version, pkg_id, int(value, 2), pkg_bin)
            return binary[len(pkg_bin) :], pkg


def read_next_operator_pkg(binary: str):
    version = int(binary[:3], 2)
    pkg_id = int(binary[3:6], 2)
    mode = binary[6]
    sub_pkg = []

    if mode == "1":
        sub_binary = binary[18:]

        for _ in range(int(binary[7:18], 2)):
            sub_binary, p = read_next_pkg(sub_binary)
            sub_pkg.append(p)

        pkg_bin = binary[: 18 + sum([len(n.binary) for n in sub_pkg])]

    else:
        sub_binary = binary[22 : 22 + int(binary[7:22], 2)]

        while sub_binary:
            sub_binary, p = read_next_pkg(sub_binary)
            sub_pkg.append(p)

        pkg_bin = binary[: 22 + sum([len(n.binary) for n in sub_pkg])]

    pkg = OperatorPackage(version, pkg_id, sub_pkg, pkg_bin)
    return (binary[len(pkg_bin) :], pkg)


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    return data.sum_version()


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    return data.value
