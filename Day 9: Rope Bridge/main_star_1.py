'''
https://adventofcode.com/2022/day/9
'''

filename = 'testinput_star_2.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line
input = filereader(filename)


class elvesBridge():
    def __init__(self):
        self.grid = []
        for i in range(500):
            self.grid.append(list("................................................................................................................................................................................................................................"))
        self.H_pos = [0, 0]  # position of head
        self.T_pos = [0, 0]  # position of tail
        self.grid[self.T_pos[0]][self.T_pos[1]] = "T"
        self.visited = []
        if self.T_pos not in self.visited: self.visited.append(list(self.T_pos))


    def printgrid(self):
        for i in range(len(self.grid)-1, -1, -1): # print in reverse order (0,0 is top left now)
            print("".join(self.grid[i]))
        print()

    def update_pos(self, move):
        dir, steps = move.strip().split(" ")
#        print(move.strip())
        for i in range(int(steps)):
            self.move_head(dir)
            delta_v = abs(self.H_pos[1] - self.T_pos[1])
            delta_h = abs(self.H_pos[0] - self.T_pos[0])
#            print("delta", delta_v, delta_h)
            if (delta_v > 1) or (delta_h > 1) or (delta_v  + delta_h > 2):
                self.move_tail(dir)

    def move_head(self, dir):
        if dir == "U": self.H_pos[0] = self.H_pos[0] + 1
        if dir == "D": self.H_pos[0] = self.H_pos[0] - 1
        if dir == "R": self.H_pos[1] = self.H_pos[1] + 1
        if dir == "L": self.H_pos[1] = self.H_pos[1] - 1
#        self.grid[self.H_pos[0]][self.H_pos[1]] = "H"
#        self.printgrid()

    def move_tail(self, dir):
#        print("dir", dir)
        deltapos_ud = abs(self.H_pos[0] - self.T_pos[0]) #row
        deltapos_lr = abs(self.H_pos[1] - self.T_pos[1]) #column
#        print("UD", deltapos_ud)
#        print("LR", deltapos_lr)
        if dir in "R":
            if self.T_pos[0] == self.H_pos[0]: #same row
                self.T_pos[1] = self.T_pos[1] + 1
            else:
                self.T_pos[1] = self.T_pos[1] + 1
                self.T_pos[0] = self.H_pos[0]
        if dir in "U":
            if self.T_pos[1] == self.H_pos[1]: #same column
                self.T_pos[0] = self.T_pos[0] + 1
            else:
                self.T_pos[0] = self.T_pos[0] + 1
                self.T_pos[1] = self.H_pos[1]
        if dir in "L":
            if self.T_pos[0] == self.H_pos[0]: #same row
                self.T_pos[1] = self.T_pos[1] - 1
            else:
                self.T_pos[0] = self.H_pos[0]
                self.T_pos[1] = self.T_pos[1] - 1
        if dir in "D":
            if self.T_pos[1] == self.H_pos[1]: #same column
                self.T_pos[0] = self.T_pos[0] - 1
            else:
                self.T_pos[0] = self.T_pos[0] - 1
                self.T_pos[1] = self.H_pos[1]
        if self.T_pos not in self.visited: self.visited.append(list(self.T_pos))

        self.grid[self.T_pos[0]][self.T_pos[1]] = "*"
#        self.printgrid()
        self.grid[self.T_pos[0]][self.T_pos[1]] = "T"
#        self.printgrid()





bridge = elvesBridge()
for step in input:
    bridge.update_pos(step)
#    bridge.printgrid()
print("star 1: ", len(bridge.visited))







