import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    players_answer = prompt.string('Your answer: ')
    return players_answer


def check_answer(players_answer, correct_answer):
    if players_answer == correct_answer:
        return True
    else:
        return False
