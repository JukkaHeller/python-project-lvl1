import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    random_number = random.randrange(1, 100)
    question = random_number
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return [question, correct_answer]
