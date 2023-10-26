import re


class Particle:
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az):
        self.pos = (x, y, z)
        self.vel = (vx, vy, vz)
        self.acc = (ax, ay, az)

    def tick(self):
        self.vel = (
            self.vel[0] + self.acc[0],
            self.vel[1] + self.acc[1],
            self.vel[2] + self.acc[2],
        )

        self.pos = (
            self.pos[0] + self.vel[0],
            self.pos[1] + self.vel[1],
            self.pos[2] + self.vel[2],
        )

    @property
    def abs_acc(self):
        return sum(abs(a) for a in self.acc)

    @property
    def dist(self):
        return sum(abs(p) for p in self.pos)


def parse_input(puzzle_input: str) -> list[Particle]:
    pattern = r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
    return [
        Particle(*[int(n) for n in match.groups()])
        for match in re.finditer(pattern, puzzle_input)
    ]


def get_closest(particles: list[Particle]):
    closest = []
    while True:
        for p in particles:
            p.tick()

        dist = list(p.dist for p in particles)
        idx = dist.index(min(dist))
        closest.append(dist.index(min(dist)))

        if len(closest) > 100 and closest.count(idx) > len(closest) / 1.25:
            return idx


def get_particels_collision(particles: list[Particle]):
    collision_free = 0
    while True:
        for p in particles:
            p.tick()
        origial_ps = len(particles)

        pos = [p.pos for p in particles]
        collision = set(p for i, p in enumerate(pos) if pos.index(p) != i)
        particles = [p for p in particles if not p.pos in collision]

        if len(particles) < origial_ps:
            collision_free = 0
        else:
            collision_free += 1

        if collision_free > 100:
            return len(particles)


def solution_1(puzzle_input: str):
    particles = parse_input(puzzle_input)
    return get_closest(particles)


def solution_2(puzzle_input: str):
    particles = parse_input(puzzle_input)
    return get_particels_collision(particles)
