class Cave:
    def __init__(self, name: str):
        self.name = name
        self.connections: Cave = []

    @classmethod
    def build_network(cls, connection_data):
        nodes = {}
        for start, end in connection_data:
            if not start in nodes:
                nodes[start] = Cave(start)

            if not end in nodes:
                nodes[end] = Cave(end)

            nodes[start].connections.append(nodes[end])
            nodes[end].connections.append(nodes[start])
        return nodes

    def islarge(self):
        return self.name.isupper()

    def find_all_pathes_to(self, end, visited: list[str] = [], double_small=False):
        """
        start
        |
        a --- b
        |     |
        c --- end
        start[] - > [[start, a,b,end],[start, a,c,end]]
            a = [start] -> [[start, a,b,end],[start, a,c,end]]
                b = [start, b] -> [[start, a,b,end]]
                    end = [start, a , b] -> [[start, a, b , end]]
                c = [start, a] -> [[start, a,c,end]]
                    end = [start, a , c] -> [[start, a, c, end]]
        """

        if self.name == end.name:
            return [visited + [self.name]]

        else:
            all_con = []

            for con in self.connections:
                new_path = visited + [self.name]

                if con.islarge() or con.name not in visited:
                    all_con.extend(con.find_all_pathes_to(end, new_path, double_small))

                elif not con.islarge() and con.name in visited and double_small:
                    small_visited_twice = any(
                        new_path.index(c) != i and c.islower()
                        for i, c in enumerate(new_path)
                    )

                    if not small_visited_twice and con.name != "start":
                        all_con.extend(
                            con.find_all_pathes_to(
                                end, visited + [self.name], double_small
                            )
                        )

            return all_con


def parse_data(puzzle_input: str) -> list[str]:
    return [n.split("-") for n in puzzle_input.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    nodes = Cave.build_network(data)
    pathes = nodes["start"].find_all_pathes_to(nodes["end"])
    return len(pathes)


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    nodes = Cave.build_network(data)
    pathes = nodes["start"].find_all_pathes_to(nodes["end"], single_cave_twice=True)
    return len(pathes)
