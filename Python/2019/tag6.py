import time
import requests

token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"


class Orbit:
    def __init__(self, name, inOrbitOf):
        self.inOrbitOf = inOrbitOf
        self.name = name
        self.orbited_by = []

    def append(self, com, name):
        if com == self.name:
            for obj in self.orbited_by:
                if name == obj.name:
                    return False
            self.orbited_by.append(Orbit(name, self))
            return True

        else:
            for n in self.orbited_by:
                if n.append(com, name):
                    return True

    def sum_depth(self, depth):
        total_depth = depth
        for obj in self.orbited_by:
            total_depth += obj.sum_depth(depth + 1)
        return total_depth

    def name_in_orbit(self, name):
        if name == self.name:
            return True
        else:
            for obj in self.orbited_by:
                if obj.name_in_orbit(name):
                    return True
        return False

    def search(self, searchname):
        if searchname == self.name:
            return self

        else:
            for obj in self.orbited_by:
                s = obj.search(searchname)
                if s is not None:
                    return s
            return None

    def orb_dist(self, searchname, dist, exclude=None):
        if searchname == self.name:
            return dist

        for obj in self.orbited_by:
            if obj != exclude:
                found = obj.orb_dist_down(searchname, dist + 1)
                if found is not None:
                    return found

        if self.inOrbitOf:
            return self.inOrbitOf.orb_dist(searchname, dist + 1, exclude=self)

        return None

    def orb_dist_down(self, searchname, dist):
        if searchname == self.name:
            return dist

        for obj in self.orbited_by:
            temp = obj.orb_dist_down(searchname, dist + 1)
            if temp is not None:
                return temp
        return None


def AOC_day5_step1():
    r = requests.get(
        "https://adventofcode.com/2019/day/6/input", cookies={"session": token}
    )
    sat_map = r.content.decode().strip().split("\n")
    print(len(sat_map))
    # sat_map= ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
    run = True
    root_COM = Orbit("COM", None)

    while run:
        run = False

        for sat_pair in sat_map:
            com, sat = sat_pair.split(")")
            if root_COM.append(com, sat):
                run = True

    print(root_COM.sum_depth(0))
    you = root_COM.search("YOU")
    print(you.orb_dist("SAN", 0) - 2)


if __name__ == "__main__":
    AOC_day5_step1()
