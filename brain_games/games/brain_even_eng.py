#!/usr/bin/env python
import random
from brain_games.games.functions import welcome_user, ask_question
from brain_games.games.functions import get_answer, check_answer


def even():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.\n'
          'Answer "yes" if the number is even, otherwise answer "no".')
    tries = 0
    for tries in range(3):
        random_number = random.randrange(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        ask_question(random_number)
        players_answer = get_answer()
        print(check_answer(players_answer, correct_answer, user_name))
        if players_answer != correct_answer:
            break
        else:
            tries += 1
