#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    random_number = random.randrange(1, 100)
    question = random_number
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return [question, correct_answer]


ask_and_check(rules, even)
