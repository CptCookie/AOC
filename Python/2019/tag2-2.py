import requests
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"


class MemOp(object):

    def __init__(self, memlist:list):
        self.memlist = memlist
        self.pointer = 0

    @property
    def instruction(self):
        return f"{self.memlist[self.pointer]:05d}"

    @property
    def opcode(self):
        return self.instruction[-2:]

    def value(self, n):
        return self.memlist[self.pointer_value(n)]

    def pointer_value(self, n):
        posmode = self.instruction[3-n] == "0"

        if posmode:
            address = self.memlist[self.pointer+n]
            return address
        else:
            return self.pointer+n

    def pointer_write(self):
        return self.memlist[self.pointer+3]


    def execute_operation(self):
        print(self.pointer)
        if self.opcode == "01":
            self.memlist[self.pointer_write()] = self.value(1) + self.value(2)
            self.pointer += 4

        elif self.opcode == "02":
            self.memlist[self.pointer_write()] = self.value(1) * self.value(2)
            self.pointer += 4

        elif self.opcode == "03":
            buffer = input("Bitte Input eingebene: ")
            self.memlist[self.pointer_value(1)] = int(buffer)
            self.pointer += 2

        elif self.opcode == "04":
            return self.value(1)
            self.pointer += 2

        elif self.opcode == "99":
            return "STOP"

    def excute_all(self):
        while True:
            rtrn = self.execute_operation()
            if rtrn is not None:
                if isinstance(rtrn, str):
                    break;
                return(rtrn)


if __name__ == "__main__":
    r = requests.get("https://adventofcode.com/2019/day/5/input", cookies={"session": token})
    aoc_input = r.content.decode().strip().split(",")
    aoc_memlist = [int(x) for x in aoc_input]
    intcomputer = MemOp(aoc_memlist)
    print(intcomputer.excute_all())



