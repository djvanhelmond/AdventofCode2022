#!/usr/local/bin/python3
from collections import defaultdict

filename = 'testinput.txt'


filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


class CRT():
    def __init__(self):
        self.cycle = 1
        self.registers = defaultdict(int)
        self.registers["X"] = 1
        self.__instr_set = {
            'noop': self.__noop,
            'addx': self.__addx,
        }
        self.grid = []
        for i in range(240):
            self.grid.append(" ")

    def draw(self):
        for i in range(0, 240, 40):
            print("".join(self.grid[i:i + 40]))


    def __noop(self):
        if self.registers["X"] <= self.cycle <= self.registers["X"] + 2:
            self.grid[self.cycle - 1] = "#"
        if self.cycle % 40 == 0:
            self.registers["X"] = self.registers["X"] + 40
        self.cycle = self.cycle + 1

    def __addx(self, val):
        if self.registers["X"] <= self.cycle <= self.registers["X"] + 2:
            self.grid[self.cycle - 1] = "#"
        if self.cycle % 40 == 0:
            self.registers["X"] = self.registers["X"] + 40
        self.cycle = self.cycle + 1
        if self.registers["X"] <= self.cycle <= self.registers["X"] + 2:
            self.grid[self.cycle - 1] = "#"
        if self.cycle % 40 == 0:
            self.registers["X"] = self.registers["X"] + 40
        self.cycle = self.cycle + 1
        self.registers["X"] = self.registers["X"] + int(val)

    def next(self, inst):
        cmd = inst.strip().split(" ")
        self.__instr_set[cmd[0]](*cmd[1:])

if __name__ == '__main__':
    input = filereader(filename)
    crt = CRT()
    for line in input:
        crt.next(line)
    crt.draw()
