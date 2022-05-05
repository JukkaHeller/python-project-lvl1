#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check, welcome_user


def gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for tries in range(3):  # 3 attempts at default
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        question = f'{random_number_1} {random_number_2}'
        # Euclid method of finding least common divisor
        while random_number_2 != 0:
            (random_number_1, random_number_2) = (
                random_number_2, random_number_1 % random_number_2)
        correct_answer = str(random_number_1)
        if ask_and_check(question, correct_answer, user_name):
            continue
        else:
            break
