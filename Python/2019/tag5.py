import requests

token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"


def process_instruction(pointer: int):
    global memlist

    param = f"{memlist[pointer]:05d}"
    opcode = param[-2:]
    value1_posm = param[-3] == "0"
    value2_posm = param[-4] == "0"

    print(f"opcode:{param} - pointer:{pointer}")

    if opcode == "01":  # add
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        memlist[memlist[pointer + 3]] = value1 + value2
        return pointer + 4

    elif opcode == "02":  # multipli
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        memlist[memlist[pointer + 3]] = value1 * value2
        return pointer + 4

    elif opcode == "03":  # read
        value1 = input("Need an Input: ")
        memlist[memlist[pointer + 1]] = int(value1)
        return pointer + 2

    elif opcode == "04":  # print
        param1 = memlist[pointer + 1]
        value1 = param1
        print(value1)
        return pointer + 2

    elif opcode == "05":  # jump if true
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        if value1 != 0:
            return value2
        return pointer + 3

    elif opcode == "06":  # jump if false
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        if value1 == 0:
            return value2
        return pointer + 3

    elif opcode == "07":  # less
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        if value1 < value2:
            memlist[memlist[pointer + 3]] = 1
        else:
            memlist[memlist[pointer + 3]] = 0
        return pointer + 4

    elif opcode == "08":  # equal
        param1 = memlist[pointer + 1]
        param2 = memlist[pointer + 2]
        print(memlist[344:])
        print(f"{param1} - {param2}")
        value1 = memlist[param1] if value1_posm else param1
        value2 = memlist[param2] if value2_posm else param2
        if value1 == value2:
            memlist[memlist[pointer + 3]] = 1
        else:
            memlist[memlist[pointer + 3]] = 0
        return pointer + 4

    elif opcode == "99":
        return None


def calc_value(pointer):
    pass


def task1():
    global memlist
    r = requests.get(
        "https://adventofcode.com/2019/day/5/input", cookies={"session": token}
    )
    memlist = r.content.decode().split(",")[:-1]
    memlist = [int(x) for x in memlist]
    print(memlist)

    pointer = 0
    while pointer is not None:
        pointer = process_instruction(pointer)

    print(memlist)


def test():
    global memlist
    memlist = [5, 1, 6, 5, 4, 9, 99, 1, 2, 0]
    pointer = 0
    while pointer is not None:
        pointer = process_instruction(pointer)

    # print(memlist)


if __name__ == "__main__":
    test()
