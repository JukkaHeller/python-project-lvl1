import random


GAME_RULE = 'What number is missing in the progression?'


def run_game():
    progression_length = random.randrange(5, 10)
    progression_gap = random.randrange(1, 4)
    progression_begin = random.randrange(5, 25)
    progression_skip = random.randrange(0, progression_length)
    progression_end = progression_begin + progression_length * progression_gap
    progression = []
    for item in range(progression_begin, progression_end + 1, progression_gap):
        progression.append(str(item))
    correct_answer = str(progression[progression_skip])
    progression[progression_skip] = '..'
    question = ' '.join(progression)
    return [question, correct_answer]
