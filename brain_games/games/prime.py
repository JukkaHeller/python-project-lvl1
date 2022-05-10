#!/usr/bin/env python
import random


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

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
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
    return [question, correct_answer]
