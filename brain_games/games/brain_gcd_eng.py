#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check


def gcd():

    rules = 'Find the greatest common divisor of given numbers.'

    def question_and_answer():
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        question = f'{random_number_1} {random_number_2}'
        # Euclid method of finding least common divisor
        while random_number_2 != 0:
            (random_number_1, random_number_2) = (
                random_number_2, random_number_1 % random_number_2)
        correct_answer = str(random_number_1)
        return [question, correct_answer]
    ask_and_check(rules, question_and_answer)
