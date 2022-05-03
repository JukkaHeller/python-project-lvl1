#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question
from brain_games.games.functions import get_answer, check_answer


def calc():
    user_name = welcome_user()
    print('What is the result of the expression?')
    for tries in range(3):
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        random_operator = random.choice(['+', '-', '*'])
        correct_answer = eval(f'{random_number_1} {random_operator} '
                              f'{random_number_2}')
        ask_question(f'{random_number_1} {random_operator} {random_number_2}')
        players_answer = int(get_answer())
        print(check_answer(players_answer, correct_answer, user_name))
        if players_answer != correct_answer:
            break
