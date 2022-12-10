'''
https://adventofcode.com/2022/day/4
'''

#filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


def fits_in(elf1, elf2):
    elf1_start, elf1_stop = elf1.split("-")
    elf2_start, elf2_stop = elf2.split("-")
    if (int(elf1_start) <= int(elf2_start)) and (int(elf1_stop) >= int(elf2_stop)):
        return True
    if (int(elf2_start) <= int(elf1_start)) and (int(elf2_stop) >= int(elf1_stop)):
        return True
    return False


def overlap(elf1, elf2):
    elf1_start, elf1_stop = elf1.split("-")
    elf2_start, elf2_stop = elf2.split("-")
    if int(elf2_start) <= (int(elf1_start) or int(elf1_stop)) <= int(elf2_stop):
        return True
    if int(elf1_start) <= (int(elf2_start) or int(elf2_stop)) <= int(elf1_stop):
        return True
    return False




puzzleinput = filereader(filename)
star_1_score = 0
star_2_score = 0
for elfs in puzzleinput:
    elf1, elf2 = elfs.strip().split(",")
    if fits_in(elf1, elf2): star_1_score = star_1_score + 1
    if overlap(elf1, elf2): star_2_score = star_2_score + 1
print("star 1: ", star_1_score)
print("star 2: ", star_2_score)


