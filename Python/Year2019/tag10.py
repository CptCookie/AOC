import requests
import numpy as np
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"

r = requests.get("https://adventofcode.com/2019/day/10/input", cookies={"session": token})
aoc_input = r.content.decode().split("\n")
aoc_input = [list(x) for  x in aoc_input]

best_coord = (0,0)
best_seeing = 0
astroids = []

for y, line in enumerate(aoc_input):
    for x, pos in enumerate(line):
        if pos == "#":
            astroids.append((x, y))

print(len(astroids))

for start in astroids:
    for end in astroids:
        if start[0] != end[0]:
            possible_loc = [for x in range[]]
        else:
            possible_loc = []





