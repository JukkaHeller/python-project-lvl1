#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check, welcome_user


"""
as we don't want user to make that much math
we can just take first couple prime numbers in range 2, 100
and compare random number to theese prime numbers
instead of realizing
for i in range(2, random_number):
    if random_number % i == 0
        return False
        break
    else:
        return True
"""


def prime():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for tries in range(3):  # 3 attempts at default
        random_number = random.randrange(2, 100)
        prime_numbers = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97
        ]
        question = random_number
        for i in prime_numbers:
            if random_number == i:
                correct_answer = 'yes'
                break
            else:
                correct_answer = 'no'
        if ask_and_check(question, correct_answer, user_name):
            continue
        else:
            break
