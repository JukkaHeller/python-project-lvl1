#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question
from brain_games.games.functions import get_answer, check_answer


def progression():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    for tries in range(3):
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
                correct_answer = progression_begin + progression_gap
                progression_begin += progression_gap
            progression += str(number) + ' '
            x += 1
        ask_question(progression)
        players_answer = int(get_answer())
        print(check_answer(players_answer, correct_answer, user_name))
        if players_answer != correct_answer:
            break
