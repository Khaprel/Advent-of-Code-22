# Rock    1 A X Lose
# Paper   2 B Y Draw
# Scissor 3 C Z Win

def calc_strat(line):
    result = 0
    if line[0] == 'A':
        if line[2] == 'X':
            result = 1 + 3
        if line[2] ==  'Y':
            result = 2 + 6
        if line[2] == 'Z':
            result = 3 + 0
    if line[0] == 'B':
        if line[2] == 'X':
            result = 1 + 0
        if line[2] ==  'Y':
            result = 2 + 3
        if line[2] == 'Z':
            result = 3 + 6
    if line[0] == 'C':
        if line[2] == 'X':
            result = 1 + 6
        if line[2] ==  'Y':
            result = 2 + 0
        if line[2] == 'Z':
            result = 3 + 3
    return result

def follow_strat(line):
    result = 0
    if line[0] == 'A':
        if line[2] == 'X':
            result = 3 + 0
        if line[2] ==  'Y':
            result = 1 + 3
        if line[2] == 'Z':
            result = 2 + 6
    if line[0] == 'B':
        if line[2] == 'X':
            result = 1 + 0
        if line[2] ==  'Y':
            result = 2 + 3
        if line[2] == 'Z':
            result = 3 + 6
    if line[0] == 'C':
        if line[2] == 'X':
            result = 2 + 0
        if line[2] ==  'Y':
            result = 3 + 3
        if line[2] == 'Z':
            result = 1 + 6
    return result

assumed_score = 0
informed_score = 0
with open('input.txt', 'r') as strategy_guide:
    for strat in strategy_guide.readlines():
        if strat.strip('\n') != '':
            assumed_score += calc_strat(strat)
            informed_score += follow_strat(strat)

print(f"The assumed strategy guide use score is {assumed_score}.")
print(f"The score according to the elf's use of the strategy guide is {informed_score}")
