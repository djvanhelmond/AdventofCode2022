'''
https://adventofcode.com/2022/day/1
'''

filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
file.close()


def star_1(game: str):
    oppo, me = game.strip().split(" ")
    #   A/X for Rock, B/Y for Paper, and C/Z for Scissors
    # All LOSSES
    if me == "X" and oppo == "B": return 0 + 1
    if me == "Y" and oppo == "C": return 0 + 2
    if me == "Z" and oppo == "A": return 0 + 3
    # All DRAWS
    if me == "X" and oppo == "A": return 3 + 1
    if me == "Y" and oppo == "B": return 3 + 2
    if me == "Z" and oppo == "C": return 3 + 3
    # All WINS
    if me == "X" and oppo == "C": return 6 + 1
    if me == "Y" and oppo == "A": return 6 + 2
    if me == "Z" and oppo == "B": return 6 + 3

def star_2(game: str):
    oppo, result = game.strip().split(" ")
    #   A for Rock, B for Paper, and C for Scissors
    #   X = lose, Y = draw, Z = win
    # All LOSSES
    if result == "X" and oppo == "A": return 0 + 3  # play scissors
    if result == "X" and oppo == "B": return 0 + 1  # play rock
    if result == "X" and oppo == "C": return 0 + 2  # play paper
    # All DRAWS
    if result == "Y" and oppo == "A": return 3 + 1  # play rock
    if result == "Y" and oppo == "B": return 3 + 2  # play paper
    if result == "Y" and oppo == "C": return 3 + 3  # play scissors
    # All WINS
    if result == "Z" and oppo == "A": return 6 + 2  # play paper
    if result == "Z" and oppo == "B": return 6 + 3  # play scissors
    if result == "Z" and oppo == "C": return 6 + 1  # play rock







star_1_score = 0
for line in lines:
    star_1_score = star_1_score + star_1(line)
print("star 1: ", star_1_score)

star_2_score = 0
for line in lines:
    star_2_score = star_2_score + star_2(line)
print("star 2: ", star_2_score)


