import prompt


TRIES_AMOUNT = 3  # 3 attempts at default


def launch(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{game.GAME_RULE}')
    for tries in range(TRIES_AMOUNT):
        question, correct_answer = game.run_game()
        print(f'Question: {question}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
