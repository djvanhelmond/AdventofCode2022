'''
https://adventofcode.com/2022/day/1
'''

filename = 'input.txt'

file = open(filename, 'r')
lines = file.readlines()
file.close()

elves = []
carry = 0

for line in lines:
    calories = line.strip()
    if calories != "":
        carry = carry + int(calories)
    else:
        elves.append(carry)
        carry = 0


print("star 1: ", max(elves))
elves.sort(reverse=True)
print("star 2: ", sum(elves[0:3]))

