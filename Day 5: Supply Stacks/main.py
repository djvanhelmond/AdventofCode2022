'''
https://adventofcode.com/2022/day/4
'''

import copy

filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


## PARSE INPUT
layout = []
moves = []
puzzleinput = filereader(filename)
line = next(puzzleinput)
while line != "\n":
    layout.append(line.strip("\n"))
    line = next(puzzleinput)
for line in puzzleinput:
    moves.append(line.strip())

# BUILD DATASTRUCTURE
containers = {}
for i in range(1, len(layout[-1].split()) + 1):
    containers[i] = []

# LOAD DATASTRUCTURE
for row in range(len(layout)-1, 0, -1):
    loadstack = 1
    for column in range(1, len(layout[row-1]), 4):
        if layout[row-1][column] != " ": containers[loadstack].append(layout[row-1][column])
        loadstack = loadstack + 1

# Make a deep copy for star2
containers_star2 = copy.deepcopy(containers)

# Execute Moves - Star 1
for line in moves:
    _, qty, _, src, _, dst = (line.split(" "))
    for _ in range(int(qty)):
        containers[int(dst)].append(containers[int(src)].pop())

star_1_answer = []
for s in containers.values():
    star_1_answer.append(s[-1])
print("star 1: ", "".join(star_1_answer))


# Execute Moves - Star 2
for line in moves:
    _, qty, _, src, _, dst = (line.split(" "))
    cache = []
    for _ in range(int(qty)):
        cache.append(containers_star2[int(src)].pop())
    for _ in range(int(qty)):
        containers_star2[int(dst)].append(cache.pop())

star_2_answer = []
for s in containers_star2.values():
    star_2_answer.append(s[-1])
print("star 2: ", "".join(star_2_answer))
