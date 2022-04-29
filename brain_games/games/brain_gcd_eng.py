#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question, \
    get_answer, check_answer


def gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    try_count = 0

    while try_count <= 2:
        correct_answer, players_answer = find_answer()
        if check_answer(players_answer, correct_answer):
            print('Correct!')
            try_count += 1
            if try_count == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"{correct_answer}'.\nLet's try again, {user_name}!")
            try_count = 3


def find_answer():
    random_number_1 = random.randrange(1, 10)
    random_number_2 = random.randrange(1, 10)
    ask_question(f'{random_number_1} {random_number_2}')
    if random_number_1 < random_number_2:
        (smaller_number, bigger_number) = (random_number_1, random_number_2)
        common_deviser = smaller_number
    elif random_number_1 > random_number_2:
        (smaller_number, bigger_number) = (random_number_2, random_number_1)
        common_deviser = smaller_number
    else:  # if random numbers are same
        least_common_deviser = random_number_1
        common_deviser = 0
    while common_deviser > 0:
        least_common_deviser = common_deviser
        common_deviser = bigger_number % smaller_number
        (smaller_number, bigger_number) = (common_deviser, smaller_number)
    correct_answer = least_common_deviser
    players_answer = int(get_answer())
    return correct_answer, players_answer
