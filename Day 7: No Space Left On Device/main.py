'''
https://adventofcode.com/2022/day/7
'''
import copy

filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line

input = filereader(filename)

pwd = ""
pwd_list = []
dirs = {}

for line in input:
    if line.startswith("$ cd"):
        if line.strip() == "$ cd /":
            pwd = ""
            pwd_list = [""]
            if pwd not in dirs: dirs[pwd] = 0
        elif line.strip() == "$ cd ..":
            pwd = "/".join(pwd_list[:-1])
            pwd_list.pop()
        else:
            arg = line.split()[-1]
            pwd_list.append(arg)
            pwd = "/".join(pwd_list)
            if pwd not in dirs: dirs[pwd] = 0
    if line[0].isdigit():
        loop_pwd_list = copy.deepcopy(pwd_list)
        while len(loop_pwd_list) != 0:
            loop_pwd = "/".join(loop_pwd_list)
            dirs[loop_pwd] = dirs[loop_pwd] + int(line.split()[0])
            loop_pwd_list.pop()

star_1_score = 0
for i in dirs.values():
    if i <= 100000:
        star_1_score = star_1_score + i
print("star 1: ", star_1_score)


todelete = 30000000 - (70000000 - dirs[''])
candidate = ''
for i in dirs:
    if dirs[i] > todelete:
        if dirs[i] < dirs[candidate]:
            candidate = i
#print("delete:", candidate)
print("star 2: ", dirs[candidate])




