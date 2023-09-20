import re
from statistics import mean


def parse_input(aoc_input: str):
    pattern = r"position=<([ \-\d]+), ([ \-\d]+)> velocity=<([ \-\d]+), ([ \-\d]+)>"
    stars = []
    for m in re.finditer(pattern, aoc_input):
        x0, y0, vx, vy = m.groups()
        stars.append((int(x0), int(y0), int(vx), int(vy)))

    return stars


def print_lights(positions):
    min_x = min([p[0] for p in positions])
    max_x = max([p[0] for p in positions]) + 1
    min_y = min([p[1] for p in positions])
    max_y = max([p[1] for p in positions]) + 1

    sky = [["\u2007" for x in range(max_x - min_x)] for y in range(max_y - min_y)]

    for p in positions:
        sky[p[1] - min_y][p[0] - min_x] = "\u2588"

    for line in sky:
        print("".join(line))


def pos_at_time(lights, time):
    return [[lx + ldx * time, ly + ldy * time] for lx, ly, ldx, ldy in lights]


def search_message(lights):
    # get an estimate of the moment for the solution, adjust for that and start simulating
    et = estimate_message_time(lights)
    et_off = 0.05  # uncertainty of the estimate

    old_pos = pos_at_time(lights, 0)
    for t in range(et - int(et_off * et), et + int(et_off * et)):
        pos = pos_at_time(lights, t)

        if calc_box_size(pos) > calc_box_size(old_pos):
            # when the area increases the lights were closest before,
            # which hints at the message beeing the last calculated state
            return old_pos, t - 1
        else:
            old_pos = pos


def estimate_message_time(lights):
    # calculate the mean center of the lights
    mean_pos_x = mean(l[0] for l in lights)
    mean_pos_y = mean(l[1] for l in lights)

    # calculate an estimated time the lights need to reach the center
    dist = [
        (max((mean_pos_x - x) / dx, (mean_pos_y - y) / dy)) for x, y, dx, dy in lights
    ]
    dist.sort()

    # return the mean of the extreams
    return int((dist[0] + dist[-1]) / 2)


def calc_box_size(pos):
    # calculate halve the cirmcumflex of the box needed to print all the lights
    min_x = min([p[0] for p in pos])
    max_x = max([p[0] for p in pos]) + 1
    min_y = min([p[1] for p in pos])
    max_y = max([p[1] for p in pos]) + 1

    return max_x - min_x + max_y - min_y


def solution_1(aoc_input: str):
    lights = parse_input(aoc_input)
    pos, t = search_message(lights)
    print_lights(pos)
    return "see the print above"


def solution_2(aoc_input: str):
    lights = parse_input(aoc_input)
    pos, t = search_message(lights)
    return t
