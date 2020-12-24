import re

pos_regex = re.compile(r'\d{1,},\d{1,}')

TOOGLE = 'toggle'
ON = 'turn on'
OFF = 'turn off'

class Lights:
    def __init__(self, bin=True):
        self.light = [0] * 1000 * 1000
        self.bin = bin
    
    @property
    def brightness(self):
        return sum(self.light)

    def actuate(self, start:[int, int], end:[int, int], action:str):
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if action == TOOGLE and self.bin:
                    self.light[x + y * 1000] = abs(self.light[x + y * 1000] -1)
                elif action == ON and self.bin:
                    self.light[x + y * 1000] = 1
                elif action == OFF and self.bin:
                    self.light[x + y * 1000] = 0
                if action == TOOGLE and not self.bin:
                    self.light[x + y * 1000] += 2
                elif action == ON and not self.bin:
                    self.light[x + y * 1000] += 1
                elif action == OFF and not self.bin:
                    self.light[x + y * 1000] -= 1 if self.light[x + y * 1000] > 0 else 0
                

def parse_line(line):
    pos = []
    for n in pos_regex.findall(line):
        x, y = n.split(',')
        pos.append([int(x), int(y)])
    
    for n in [TOOGLE, OFF, ON]:
        if n in line:
            return pos + [n]

def test_turning_lights():
    l = Lights()
    l.actuate([0,0], [2,2], ON)
    assert l.brightness == 9
    l.actuate([1,1], [2,2], TOOGLE)
    assert l.brightness == 5
    l.actuate([0,0], [0,0], OFF)
    assert l.brightness == 4

def test_turning_lights_bright():
    l = Lights(bin=False)
    l.actuate([0,0], [0,0], ON)
    assert l.brightness == 1
    l.actuate([0,0], [999,999], TOOGLE)
    assert l.brightness == 2000001

def test_parse():
    assert parse_line('toggle 173,401 through 496,407') == [[173,401],[496,407],TOOGLE]
    assert parse_line('turn on 313,306 through 363,621') == [[313,306],[363,621],ON]
    assert parse_line('turn off 61,44 through 567,111') == [[61,44],[567,111],OFF]

def solve(puzzle_input):
    print('testing ', end='')
    test_parse()
    test_turning_lights()
    test_turning_lights_bright()
    print('done')

    print('\nsolving')
    deko = Lights()
    for n, line in enumerate([n for n in puzzle_input.split('\n') if n != '']):
        deko.actuate(*parse_line(line))
    print(f'solution 1: {deko.brightness}')

    deko = Lights(bin=False)
    for n, line in enumerate([n for n in puzzle_input.split('\n') if n != '']):
        deko.actuate(*parse_line(line))
    print(f'solution 2: {deko.brightness}')