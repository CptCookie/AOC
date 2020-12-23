import requests
import numpy as np
letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"
r = requests.get("https://adventofcode.com/2019/day/3/input", cookies={"session": token})
input = r.content.decode().split("\n")
wire1 = input[0].split(",")
wire2 = input[1].split(",")

# wire1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L7"]
# wire2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
#
# wire1 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
# wire2 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

def calc_coord(wire):
    coords = [(0,0)]

    for instr in wire:
        start = coords[-1]
        path = None
        if instr[0] == "R":
            path = [(start[0]+x, start[1]) for x in range( int(instr[1:])+1 )][1:]
        if instr[0] == "L":
            path= [(start[0]-x, start[1]) for x in range( int(instr[1:])+1 )][1:]
        if instr[0] == "U":
            path = [(start[0], start[1]+y) for y in range( int(instr[1:])+1 )][1:]
        if instr[0] == "D":
            path = [(start[0], start[1]-y) for y in range( int(instr[1:])+1 )][1:]

        for n in path:
            coords.append(n)

    return(coords)


coord_wire1 = calc_coord(wire1)
coord_wire2 = calc_coord(wire2)
crosses_coord = set(coord_wire1) & set(coord_wire2)
crosses = []

for n in crosses_coord:
    crosses.append((abs(n[0]) + abs(n[1]), coord_wire1.index(n) + coord_wire2.index(n)))

print(crosses)
print(min(crosses))
print(sorted(crosses, key=lambda tup: tup[1]))
# for m,n in enumerate(coord_wire1):
#     print(f"{m/(len(coord_wire1)+1)*100}%")
#     if n in coord_wire2:
#         crosses.append(n)
#
# print(crosses)
