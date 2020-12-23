import requests
import copy
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"

test1 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]  # == 8->1
test2 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]  # <= 8->1
test3 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]  # == 8->1
test4 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]  # <= 8->1
test5 = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]  # == 0->1
test6 = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]  # == 0->1
test7 = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,  # < 8->999
         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,  # == 8->1000
         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]  # > 8->1001

class IntcodeComputer:

    def __init__(self, memlist):
        self.memlist = memlist
        self.pointer = 0

    def set_input(self, userinput):
        self.userinput = userinput

    def get_output(self):
        return(self.useroutput)

    @property
    def instruct(self):
        return f"{self.memlist[self.pointer]:05d}"

    @property
    def op_code(self):
        return self.instruct[-2:]

    @property
    def addr1(self):
        if self.instruct[2] == "1": return self.pointer + 1
        else: return self.memlist[self.pointer + 1]

    @property
    def addr2(self):
        if self.instruct[1] == "1": return self.pointer + 2
        else: return self.memlist[self.pointer + 2]

    @property
    def addr3(self):
        if self.instruct[0] == "1": return self.pointer + 3
        else: return self.memlist[self.pointer + 3]


    @property
    def value1(self):
        return self.memlist[self.addr1]

    @property
    def value2(self):
        return self.memlist[self.addr2]

    @property
    def value3(self):
        return self.memlist[self.addr3]

    def excecute(self):
        # print(self.pointer)
        if self.op_code == "01":
            self.memlist[self.addr3] = self.value1 + self.value2
            self.pointer += 4

        elif self.op_code == "02":
            self.memlist[self.addr3] = self.value1 * self.value2
            self.pointer += 4

        elif self.op_code == "03":
            self.memlist[self.addr1] = self.userinput
            self.pointer += 2

        elif self.op_code == "04":
            self.useroutput = self.value1
            self.pointer += 2

        elif self.op_code == "05":
            if self.value1 != 0:
                self.pointer = self.value2
            else:
                self.pointer += 3

        elif self.op_code == "06":
            if self.value1 == 0:
                self.pointer = self.value2
            else:
                self.pointer += 3

        elif self.op_code == "07":
            self.memlist[self.addr3] = 1 if self.value1 < self.value2 else 0
            self.pointer += 4

        elif self.op_code == "08":
            self.memlist[self.addr3] = 1 if self.value1 == self.value2 else 0
            self.pointer += 4

        elif self.op_code == "99":
            raise StopIteration

    def run(self):
        while self.pointer < len(self.memlist):
            # print(self.pointer)
            try:
                self.excecute()
            except StopIteration:
                break

def test(instr, test_input):
    c = IntcodeComputer(instr)
    c.set_input(test_input)
    c.run()
    return c.get_output()

def test_cases():
    assert test(copy.deepcopy(test1), 7) == 0
    assert test(copy.deepcopy(test1), 8) == 1
    assert test(copy.deepcopy(test2), 7) == 1
    assert test(copy.deepcopy(test2), 8) == 0
    assert test(copy.deepcopy(test3), 7) == 0
    assert test(copy.deepcopy(test3), 8) == 1
    assert test(copy.deepcopy(test4), 7) == 1
    assert test(copy.deepcopy(test4), 8) == 0
    assert test(copy.deepcopy(test5), 0) == 0
    assert test(copy.deepcopy(test5), 1) == 1
    assert test(copy.deepcopy(test6), 0) == 0
    assert test(copy.deepcopy(test6), 1) == 1
    assert test(copy.deepcopy(test7), 7) == 999
    assert test(copy.deepcopy(test7), 8) == 1000
    assert test(copy.deepcopy(test7), 9) == 1001


if __name__ == "__main__":
    r = requests.get("https://adventofcode.com/2019/day/5/input", cookies={"session": token})
    instructions = r.content.decode().split(",")[:-1]
    instructions = [int(x) for x in instructions]

    calculator = IntcodeComputer(instructions)
    calculator.set_input(5)
    calculator.run()
    print(calculator.get_output())
