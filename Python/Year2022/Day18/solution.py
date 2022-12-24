class Obsidian:

    ADJACENT = [
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0),
    ]

    def __init__(self, voxel):
        self.voxel = voxel
        self.min_x, self.max_x = 1000, 0
        self.min_y, self.max_y = 1000, 0
        self.min_z, self.max_z = 1000, 0
        for x, y, z in self.voxel:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)

            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)

            self.min_z = min(self.min_z, z)
            self.max_z = max(self.max_z, z)

    def total_surface(self):
        surface = 0
        for cx, cy, cz in self.voxel:
            for dx, dy, dz in self.ADJACENT:
                if not (cx + dx, cy + dy, cz + dz) in self.voxel:
                    surface += 1
        return surface

    def get_start(self):
        highest = [(x, y, z) for x, y, z in self.voxel if y == self.max_y][0]
        return (highest[0], highest[1] + 1, highest[2])

    def outer_surface(self):
        surface = 0
        done = set()
        open = set([self.get_start()])

        while open:
            vx, vy, vz = open.pop()
            done.add((vx, vy, vz))

            for dx, dy, dz in self.ADJACENT:
                dv = (vx + dx, vy + dy, vz + dz)
                x_in_limit = self.min_x - 1 <= dv[0] <= self.max_x + 1
                y_in_limit = self.min_y - 1 <= dv[1] <= self.max_y + 1
                z_in_limit = self.min_z - 1 <= dv[2] <= self.max_z + 1
                in_limit = x_in_limit and y_in_limit and z_in_limit

                if (
                    dv not in open
                    and dv not in done
                    and dv not in self.voxel
                    and in_limit
                ):
                    open.add(dv)

        for x, y, z in done:
            for dx, dy, dz in self.ADJACENT:
                if (dx + x, dy + y, dz + z) in self.voxel:
                    surface += 1
        return surface


def parse_input(puzzle_input: str) -> set[tuple[int]]:
    return set(
        tuple(int(c) for c in n.split(","))
        for n in puzzle_input.splitlines()
        if n != ""
    )


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    obs = Obsidian(input)
    return obs.total_surface()


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    obs = Obsidian(input)
    return obs.outer_surface()
