#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check


rules = 'What number is missing in the progression?'


def progression():
    progression_length = random.randrange(5, 10)
    progression_gap = random.randrange(1, 4)
    progression_begin = random.randrange(5, 25)
    progression_skip = random.randrange(1, progression_length)
    progression = ''
    for x in range(progression_length):
        if x != progression_skip:
            number = progression_begin + progression_gap
            progression_begin = number
        else:
            number = '..'
            correct_answer = str(progression_begin + progression_gap)
            progression_begin += progression_gap
        progression += str(number) + ' '
        x += 1
    question = progression
    return [question, correct_answer]


ask_and_check(rules, progression)
