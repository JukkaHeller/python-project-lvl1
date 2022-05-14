import random
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    random_number = random.randrange(2, 100)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    question = random_number
    return [question, correct_answer]


def is_prime(number):
    divisor = 2
    if number < 2:
        return False
    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            return False
        divisor += 1
    return True
