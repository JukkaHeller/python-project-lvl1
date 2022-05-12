import random


RULES = 'Find the greatest common divisor of given numbers.'


def run_game():
    random_number_1 = random.randrange(1, 100)
    random_number_2 = random.randrange(1, 100)
    question = f'{random_number_1} {random_number_2}'
    # Euclid method of finding least common divisor
    correct_answer = count_gcd(random_number_1, random_number_2)
    return [question, correct_answer]


def count_gcd(number_1, number_2):
    while number_2 != 0:
        (number_1, number_2) = (number_2, number_1 % number_2)
    return str(number_1)
