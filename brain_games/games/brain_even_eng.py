#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check, welcome_user


def even():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for tries in range(3):  # 3 attempts at default
        random_number = random.randrange(1, 100)
        question = random_number
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if ask_and_check(question, correct_answer, user_name):
            continue
        else:
            break
