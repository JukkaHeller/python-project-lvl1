#!/usr/bin/env python
import prompt


def ask_and_check(game):
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{game.rules}')
    tries_amount = 3  # 3 attempts at default
    for tries in range(tries_amount):
        question, correct_answer = game.game()
        print(f'Question: {question}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == correct_answer:
            print(f'Congratulations, {user_name}!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            break
