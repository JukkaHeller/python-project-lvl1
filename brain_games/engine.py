import prompt


TRIES_AMOUNT = 3  # 3 attempts at default


def launch(run_game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{run_game.RULES}')
    for tries in range(TRIES_AMOUNT):
        question, correct_answer = run_game.run_game()
        print(f'Question: {question}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            break
        if tries == TRIES_AMOUNT - 1:
            print(f'Congratulations, {user_name}!')
