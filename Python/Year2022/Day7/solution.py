class Dir:
    def __init__(self, name):
        self.name = name
        self.children = []

    @property
    def size(self):
        return sum(c.size for c in self.children)


class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)


def parse_data(puzzle_input: str) -> list[str]:
    files = {"/": Dir("/")}
    current_dir = "/"

    for line in puzzle_input.splitlines()[1:]:
        if "$" in line:
            if "ls" in line and not "cd" in line:
                pass

            elif ".." in line:
                current_dir = "/".join(current_dir.split("/")[:-1])

            else:
                goto = line.split(" ")[2]
                current_dir = current_dir + "/" + goto

        elif not "$" in line:
            if "dir" in line:
                name = line.split(" ")[1]
                folder = Dir(name)
                files[current_dir].children.append(folder)
                files[f"{current_dir}/{name}"] = folder

            else:
                size, name = line.split(" ")
                f = File(size, name)
                files[current_dir].children.append(f)
                files[f"{current_dir}/{name}"] = f

    return files


def solution_1(puzzle_input: str):
    dir_tree = parse_data(puzzle_input)
    return sum(
        node.size
        for node in dir_tree.values()
        if node.size <= 100000 and node.__class__ == Dir
    )


def solution_2(puzzle_input: str):
    dir_tree = parse_data(puzzle_input)
    c_free = 70_000_000 - dir_tree["/"].size
    return sorted([f.size for f in dir_tree.values() if c_free + f.size >= 30_000_000])[
        0
    ]
