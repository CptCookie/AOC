from copy import deepcopy
import re

class Programm:
    def __init__(self, instructions):
        self.instr = [n.replace('-> ', '').split(' ') for n in instructions]
        for n, elem in enumerate(self.instr):
            self.instr[n] = [int(m) if re.match(r'\d', m) else m for m in elem]
        self.mem = {}
    
    def _set(self, key, value):
        if type(value) == str and value in self.mem:
            self.mem.update({key: self.mem[value]})
            return True
        elif type(value) == int:
            self.mem.update({key: value})
            return True
    
    def _not(self, arg, to:str):
        if type(arg) == str and arg in self.mem:
            self.mem.update({to: 65535 - self.mem[arg]})
            return True
        elif type(arg) == int:
            self.mem.update({to: 65535 - arg})
            return True

    def _and(self, arg_1:str , arg_2:str , to:str):
        if type(arg_1) == str and arg_1 in self.mem and arg_2 in self.mem:
            self.mem.update({to: self.mem[arg_1] & self.mem[arg_2]})
            return True
        elif type(arg_1) == int and arg_2 in self.mem:
            self.mem.update({to: arg_1 & self.mem[arg_2]})
            return True
    
    def _or(self, arg_1:str , arg_2:str , to:str):
        if type(arg_1) == str and arg_1 in self.mem and arg_2 in self.mem:
            self.mem.update({to: self.mem[arg_1] | self.mem[arg_2]})
            return True
        elif type(arg_1) == int and arg_2 in self.mem:
            self.mem.update({to: arg_1 | self.mem[arg_2]})
            return True
    
    def _lshift(self, addr:str, number:int, to:str):
        if addr in self.mem:
            self.mem.update({to: self.mem[addr] << number})
            return True

    def _rshift(self, addr:str, number:int, to:str):
        if addr in self.mem:
            self.mem.update({to: self.mem[addr] >> number})
            return True

    def run(self):
        while len(self.instr) > 0:
            buffer_instr = deepcopy(self.instr)

            for n,line in enumerate(self.instr):
                executed = False
                if len(line) == 2:
                    executed = self._set(line[1], line[0])
                elif len(line) == 3 and line[0] == 'NOT':
                    executed = self._not(line[1], line[2])
                elif line[1] == 'RSHIFT':
                    executed = self._rshift(line[0], line[2], line[3])
                elif line[1] == 'LSHIFT':
                    executed = self._lshift(line[0], line[2], line[3])
                elif line[1] == 'AND':
                    executed = self._and(line[0], line[2], line[3])
                elif line[1] == 'OR' and line[0]:
                    executed = self._or(line[0], line[2], line[3])
                if executed:
                    buffer_instr.pop(n)
                    break
            
            if len(buffer_instr) == 0:
                return
            elif len(buffer_instr) == len(self.instr):
                raise Exception('Can not resolve all Instructions')
            else:
                self.instr = buffer_instr

        
def test_execute():
    instruction = [
        '1 -> a',
        'a LSHIFT 1 -> b',
        'a OR b -> c'
    ]
    prog = Programm(instruction)
    prog.run()
    assert prog.mem == {'a': 1, 'b': 2, 'c': 3}

    instruction = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    prog = Programm(instruction)
    prog.run() 
    assert prog.mem == { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456, }


def solve(puzzle_input):
    print('testing ', end='')
    test_execute()
    print('done')

    print('solving')
    prog = Programm([n for n in puzzle_input.split('\n') if n != ''])
    prog.run()
    a = prog.mem['a']
    print(f'solution 1: {a}')

    instr = [n for n in puzzle_input.split('\n') if n != '']
    for n, line in enumerate(instr):
        if re.match('\d+ -> b', line):
            instr[n] = f'{a} -> b'

    prog = Programm(instr)
    prog.run()
    a = prog.mem['a']
    print(f'solution 2: {a}')