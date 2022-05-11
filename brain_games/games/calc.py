#!/usr/bin/env python
import random
import operator


rules = 'What is the result of the expression?'


def game():
    random_number_1 = random.randrange(1, 100)
    random_number_2 = random.randrange(1, 100)
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    picked_operator = random.choice(list(operators.keys()))
    question = f"{random_number_1} {picked_operator} {random_number_2}"
    correct_answer = str(
        operators.get(picked_operator)(random_number_1, random_number_2))
    return [question, correct_answer]
