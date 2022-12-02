with open("./inputs/day2.txt") as f:
    all_rounds = f.readlines()

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

correct_choices = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

wrong_choices = {
    "A":"Z",
    "B":"X",
    "C":"Y"
}


draws = {
    "A": "X",     # rock
    "B": "Y",     # paper
    "C": "Z"      # scissors
}

tweaked_scores = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


"""
0 -> lost
3 -> draw
6 -> won


A Y
B X
C Z

"""

# Part 2
score = 0
for round in all_rounds:
    opponent, mine = round.split()

    if mine=="Y":
        choose = draws[opponent]
    elif mine=="Z":
        choose = correct_choices[opponent]
    else:
        choose = wrong_choices[opponent]

    # print("opponent", opponent)
    # print("What to do?", mine)
    # print("Choose", choose)
    # print("tweaked_scores", tweaked_scores[mine])
    # print("score of choosing", scores[choose])
    score += tweaked_scores[mine] + scores[choose]
    # print(score)

print(score)

# Part 1
score = 0
for round in all_rounds:
    opponent, mine = round.split()

    if draws[opponent]==mine:
        score += 3 + scores[mine]
    elif correct_choices[opponent] == mine:
        score += 6 + scores[mine]
    else:
        score += scores[mine]

print(score)
