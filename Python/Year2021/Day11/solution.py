class DumboFishSwarm:
    def __init__(self, init_state) -> None:
        self.swarm = init_state
        self.height = len(self.swarm)
        self.width = len(self.swarm[0])

    def get_adjacent_points(self, x: int, y: int) -> list[tuple[int]]:
        adj = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if 0 <= x + dx <= self.width - 1 and 0 <= y + dy <= self.height - 1:
                    if dx != 0 or dy != 0:
                        adj.append((x + dx, y + dy))
        return adj

    def add_1(self):
        for y in range(self.height):
            for x in range(self.width):
                self.swarm[y][x] += 1

    def flash(self, x: int, y: int):
        adj = self.get_adjacent_points(x, y)
        for point in adj:
            if self.swarm[point[1]][point[0]] != 0:
                self.swarm[point[1]][point[0]] += 1
        self.swarm[y][x] = 0

    def step(self):
        flash_counter = 0
        self.add_1()

        while any(fish > 9 for line in self.swarm for fish in line):
            for x in range(self.width):
                for y in range(self.height):
                    if self.swarm[y][x] > 9:
                        self.flash(x, y)
                        flash_counter += 1

        return flash_counter

    def search_sync_flash(self):
        for n in range(500):
            if self.step() == self.height * self.width:
                return n + 1


def parse_data(puzzle_input: str) -> list[str]:
    data = []
    for line in puzzle_input.splitlines():
        if line != "":
            data.append([int(n) for n in line if n != ""])
    return data


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    swarm = DumboFishSwarm(data)
    flash_counter = 0

    for i in range(100):
        flash_counter += swarm.step()

    return flash_counter


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    swarm = DumboFishSwarm(data)
    return swarm.search_sync_flash()
