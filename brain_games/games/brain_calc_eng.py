#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_and_check


def calc():
    user_name = welcome_user()
    print('What is the result of the expression?')
    for tries in range(3):  # 3 attempts at default
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        random_operator = random.choice(['+', '-', '*'])
        question = f'{random_number_1} {random_operator} {random_number_2}'
        correct_answer = str(eval(f'{random_number_1} {random_operator} '
                                  f'{random_number_2}'))
        if ask_and_check(question, correct_answer, user_name):
            continue
        else:
            break
