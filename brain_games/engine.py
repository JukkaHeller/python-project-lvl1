#!/usr/bin/env python
import prompt


TRIES_AMOUNT = 3  # 3 attempts at default


def launch(game):
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{game.rules}')
    for tries in range(TRIES_AMOUNT):
        question, correct_answer = game.game()
        print(f'Question: {question}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == correct_answer:
            print(f'Congratulations, {user_name}!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            break
