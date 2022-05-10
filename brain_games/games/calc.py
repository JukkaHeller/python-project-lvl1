#!/usr/bin/env python
import random


rules = 'What is the result of the expression?'


def game():
    random_number_1 = random.randrange(1, 100)
    random_number_2 = random.randrange(1, 100)
    random_operator = random.choice(['+', '-', '*'])
    question = f"{random_number_1} {random_operator} {random_number_2}"
    correct_answer = str(eval(question))
    return [question, correct_answer]
