#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question
from brain_games.games.functions import get_answer, check_answer


def gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for tries in range(3):
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        correct_answer = find_answer(random_number_1, random_number_2)
        ask_question(f'{random_number_1} {random_number_2}')
        players_answer = int(get_answer())
        print(check_answer(players_answer, correct_answer, user_name))
        if players_answer != correct_answer:
            break


# Euclid method of finding least common deviser
def find_answer(random_number_1, random_number_2):
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
#    print(correct_answer)
    return correct_answer
