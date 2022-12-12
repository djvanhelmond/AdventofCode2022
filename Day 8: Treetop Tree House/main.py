'''
https://adventofcode.com/2022/day/7
'''

filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


def is_visible(trees, row, column):
    left_visible = right_visible = top_visible = bottom_visible = True
    for left in range(0, column):
        if trees[row][left] >= trees[row][column]: left_visible = False
    for right in range(column + 1, len(trees[0])):
        if trees[row][right] >= trees[row][column]: right_visible = False
    for top in range(0, row):
        if trees[top][column] >= trees[row][column]: top_visible = False
    for bottom in range(row + 1, len(trees)):
        if trees[bottom][column] >= trees[row][column]: bottom_visible = False
    if bottom_visible or top_visible or right_visible or left_visible:
        return True
    return False


def calc_viewing_distance(trees, row, column):
    left_distance = top_distance = right_distance = bottom_distance = 1
    lefttrees = []
    for left in range(0, column):
        lefttrees.append(trees[row][left])
    while lefttrees[-1] < trees[row][column] and len(lefttrees) != 1:
        lefttrees.pop()
        left_distance = left_distance + 1
    toptrees = []
    for top in range(0, row):
        toptrees.append(trees[top][column])
    while toptrees[-1] < trees[row][column] and len(toptrees) != 1:
        toptrees.pop()
        top_distance = top_distance + 1
    righttrees = []
    for right in range(len(trees[0])-1, column, -1):
        righttrees.append(trees[row][right])
    while righttrees[-1] < trees[row][column] and len(righttrees) != 1:
        righttrees.pop()
        right_distance = right_distance + 1
    bottomtrees = []
    for bottom in range(len(trees)-1, row, -1):
        bottomtrees.append(trees[bottom][column])
    while bottomtrees[-1] < trees[row][column] and len(bottomtrees) != 1:
        bottomtrees.pop()
        bottom_distance = bottom_distance + 1
    total = left_distance * right_distance * top_distance * bottom_distance
    return total


trees = []
input = filereader(filename)
for row in input:
    trees.append(list(row.strip()))


visible = (len(trees[0])+len(trees[0])-2)*2
for row in range(1, len(trees)-1):
    for column in range(1, len(trees[0])-1):
        if is_visible(trees, row, column):
            visible = visible + 1
print("star 1: ", visible)

highest_scenic_score = 0
for row in range(1, len(trees)-1):
    for column in range(1, len(trees[0])-1):
        scenic_score = calc_viewing_distance(trees, row, column)
        if scenic_score > highest_scenic_score: highest_scenic_score = scenic_score
print("star 2: ", highest_scenic_score)




