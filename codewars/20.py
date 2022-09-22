# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
def score(dice):
    summa = 0
    for n in set(dice):
        if dice.count(n) > 2:
            if n == 1:
                summa += 1000
                if dice.count(n) == 4:
                    summa += 100
                if dice.count(n) == 5:
                    summa += 200


print(score([2, 3, 4, 6, 2]))
