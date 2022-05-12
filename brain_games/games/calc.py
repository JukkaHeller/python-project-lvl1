import random


RULES = 'What is the result of the expression?'


def run_game():
    random_number_1 = random.randrange(1, 100)
    random_number_2 = random.randrange(1, 100)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    question = f"{random_number_1} {random_operator} {random_number_2}"
    if random_operator == '+':
        correct_answer = str(random_number_1 + random_number_2)
    elif random_operator == '-':
        correct_answer = str(random_number_1 - random_number_2)
    else:
        correct_answer = str(random_number_1 * random_number_2)
    return [question, correct_answer]
