import requests
token = "53616c7465645f5f714a6cdb587039fed75269df026ce7ed488de790cdf65fd96d06ec495e5b02c1551c3f2b487d59d5"
r = requests.get("https://adventofcode.com/2019/day/1/input", cookies={"session": token})
input = r.content.decode().split("\n")

def easyfuel(modules):
    fuel = 0
    for n in modules[:-1]:
        print(f"module - {n}")
        fuel += int(int(n) / 3 - 2)
    return fuel

def fuel_consumtion(mass):
    return int(mass / 3 - 2)

def nextfuel(modules):
    tank = 0
    for n in modules[:-1]:
        addfuel = fuel_consumtion(int(n))
        tank += addfuel
        while True:
            addfuel = fuel_consumtion(addfuel)
            if addfuel > 0:
                tank += addfuel
            else: break
    return tank

print(nextfuel(input))