### 
### self check: random shakespear
### goal randomly generate 28 characters such that
### eventually return the goal string:
### "methinks it is like a weasel"

from string import ascii_lowercase
import random

## function 1: randomly generate a string of 28 characters from 26 letters plus the space
# create a pool of chars

goal_line = "methinks it is like a weasel"


def generate_line(n):
    chars = [" "]
    for i in ascii_lowercase:
        chars.append(i)

    line = ''
    for count in range(n):
        i = random.randrange(0,len(chars))
        line = line + chars[i]

    return line

## function 2: loss - score generated candidate to goal

new_line = generate_line(len(goal_line))

def score_loss(new_line):
    if len(new_line) != len(goal_line):
        return "lines not of equal length."
    else:
        score = 0
        for i in range(len(goal_line)):
            if new_line[i] != goal_line[i]:
                score = score + 1
    #        return score
        return score

#score = score_loss(new_line)
#print(score)

## function 3: repetition untill success
def get_goal(goal_line):
    count = 0
    score = -1 #initialize
    while score != 0:
        new_line = generate_line(len(goal_line))
        score = score_loss(new_line)
        count = count + 1


    return new_line,count



