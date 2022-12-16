#!/usr/local/bin/python3
from collections import defaultdict

filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


class CRT():
    def __init__(self):
        self.cycle = 0
        self.registers = defaultdict(int)
        self.registers["X"] = 1
        self.__instr_set = {
            'noop': self.__noop,
            'addx': self.__addx,
        }
        self.sum = 0

    def __noop(self):
        self.cycle = self.cycle + 1
        if self.cycle % 40 == 20:
            self.sum = self.sum + (self.cycle * self.registers["X"])


    def __addx(self, val):
        self.cycle = self.cycle + 1
        if self.cycle % 40 == 20:
            self.sum = self.sum + (self.cycle * self.registers["X"])
        self.cycle = self.cycle + 1
        if self.cycle % 40 == 20:
            self.sum = self.sum + (self.cycle * self.registers["X"])
        self.registers["X"] = self.registers["X"] + int(val)

    def next(self, inst):
        cmd = inst.strip().split(" ")
        self.__instr_set[cmd[0]](*cmd[1:])



if __name__ == '__main__':
    input = filereader(filename)
    crt = CRT()
    for line in input:
        crt.next(line)
    print("Star 1: ", crt.sum)








