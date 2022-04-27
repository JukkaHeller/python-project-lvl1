#!/usr/bin/env python
import random
from brain_games.engine import welcome_user, ask_question, \
    get_answer, check_answer


def calc():

    user_name = welcome_user()
    print('What is the result of the expression?')

    try_count = 0

    while try_count <= 2:
        random_number_1 = random.randrange(1, 10)
        random_number_2 = random.randrange(1, 10)
        operators = ['+', '-', '*']
        random_operator = random.choice(operators)
        correct_answer = eval(f'{random_number_1} {random_operator} '
                              f'{random_number_2}')
        ask_question(f'{random_number_1} {random_operator} {random_number_2}')
        players_answer = get_answer()
        if check_answer(str(players_answer), str(correct_answer)):
            print('Correct!')
            try_count += 1
            if try_count == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"{correct_answer}'.\nLet's try again, {user_name}!")
            try_count = 3


def main():
    calc()


if __name__ == '__main__':
    main()
