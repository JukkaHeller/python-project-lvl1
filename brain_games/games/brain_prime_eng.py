#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question
from brain_games.games.functions import get_answer, check_answer


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
    for tries in range(3):
        random_number = random.randrange(2, 100)
        prime_numbers = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97
        ]
        ask_question(random_number)
        players_answer = get_answer()
        for i in prime_numbers:
            if random_number == i:
                correct_answer = 'yes'
                break
            else:
                correct_answer = 'no'
        print(check_answer(players_answer, correct_answer, user_name))
        if players_answer != correct_answer:
            break
