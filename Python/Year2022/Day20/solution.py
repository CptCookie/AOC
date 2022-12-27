class Node:
    def __init__(self, value: int | str):
        self.value = int(value)
        self.prev = None
        self.next = None

    def move(self):
        if self.value > 0:
            self.__move_next()
        elif self.value < 0:
            self.__move_prev()

    def __move_next(self):
        link = self
        for n in range(self.value):
            link = link.next

        # remove self from list
        self.prev.next = self.next
        self.next.prev = self.prev

        #       self
        #     /      \
        # link ------ next
        self.next = link.next
        self.prev = link

        #       self
        #     /      \
        # link         next
        link.next.prev = self
        link.next = self

    def __move_prev(self):
        link = self
        for n in range(abs(self.value)):
            link = link.prev

        # remove self from list
        self.prev.next = self.next
        self.next.prev = self.prev

        #       self
        #     /      \
        # prev ------ link
        self.next = link
        self.prev = link.prev

        #       self
        #     /      \
        # link         next
        link.prev.next = self
        link.prev = self

def parse_input(puzzle_input: str) -> list[Node]:
    nodes = []
    for i, value in enumerate(puzzle_input.splitlines()):
        if value != "":
            n = Node(value)
            if i > 0:
                n.prev = nodes[i-1]
                nodes[i - 1].next = n
            nodes.append(n)
    nodes[0].prev = nodes[-1]
    nodes[-1].next = nodes[0]
    return nodes

def mix_decrypt(nodes, rounds=1):
    for node in nodes:
        node.move()

def get_grove_coordinates(nodes, rounds=1):
    for n in range(rounds):
        mix_decrypt(nodes)

    numbers = []

    for n in nodes:
        if n.value == 0:
            link = n
            break

    for i in range(3001):
        if i in [1000, 2000, 3000]:
            numbers.append(link.value)
        link = link.next

    return sum(numbers)


def solution_1(puzzle_input: str):
    nodes = parse_input(puzzle_input)
    return get_grove_coordinates(nodes, 1)



def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    return None
