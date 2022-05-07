#!/usr/bin/env python
import random
from brain_games.games.functions import ask_and_check


def calc():
    rules = 'What is the result of the expression?'

    def question_and_answer():
        random_number_1 = random.randrange(1, 100)
        random_number_2 = random.randrange(1, 100)
        random_operator = random.choice(['+', '-', '*'])
        question = f"{random_number_1} {random_operator} {random_number_2}"
        correct_answer = str(eval(question))
        return [question, correct_answer]
    ask_and_check(rules, question_and_answer)
