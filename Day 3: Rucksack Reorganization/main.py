'''
https://adventofcode.com/2022/day/3
'''

filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line

def getprio(letter:str):
    if 65 <= ord(letter[0]) <= 90:
        return ord(letter[0])-38
    if 97 <= ord(letter[0]) <= 122:
        return ord(letter[0])-96


puzzleinput = filereader(filename)
star_1_score = 0
for line in puzzleinput:
    comp_1 = list(line.strip()[0:int(len(line)/2)])
    comp_2 = list(line.strip()[int(len(line)/2)::])
    inboth = list(set(comp_1).intersection(comp_2))[0]
    star_1_score = star_1_score + getprio(inboth)

print("star 1: ", star_1_score)


puzzleinput = filereader(filename)
star_2_score = 0
for line in puzzleinput:
    bag_1 = list(line.strip())
    bag_2 = list(next(puzzleinput).strip())
    bag_3 = list(next(puzzleinput).strip())
    inall = list(set(bag_1).intersection(bag_2).intersection(bag_3))[0]
    star_2_score = star_2_score + getprio(inall)

print("star 2: ", star_2_score)
