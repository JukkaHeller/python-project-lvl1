import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def ask_and_check(question, correct_answer, user_name):
    print(f'Question: {question}')
    players_answer = prompt.string('Your answer: ')
    if players_answer == correct_answer:
        print(f'Congratulations, {user_name}!')
        return True
    else:
        print(f"'{players_answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.\nLet's try again, {user_name}!")
        return False
