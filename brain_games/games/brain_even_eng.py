#!/usr/bin/env python
import random
import prompt


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    answer_is_even = 'yes'
    answer_is_odd = 'no'
    try_count = 0
    print(f'Answer "{answer_is_even}" if the number is even, '
          f'otherwise answer "{answer_is_odd}".')
    while try_count <= 2:
        random_number = random.randrange(1, 100)
        is_even = random_number % 2 == 0 and True
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if (is_even and answer == answer_is_even) \
                or (not is_even and answer == answer_is_odd):
            print('Correct!')
            try_count += 1
            if try_count == 3:
                print(f'Congratulations, {name}!')
        elif is_even and answer != answer_is_even:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"{answer_is_even}'.\nLet's try again, {name}!")
            try_count = 3
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"{answer_is_odd}'.\nLet's try again, {name}!")
            try_count = 3
