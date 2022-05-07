#!/usr/bin/env python
import prompt


def ask_and_check(rules, question_and_answer):
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{rules}')
    for tries in range(3):  # 3 attempts at default
        question, correct_answer = question_and_answer()
        print(f'Question: {question}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == correct_answer:
            print(f'Congratulations, {user_name}!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            break
