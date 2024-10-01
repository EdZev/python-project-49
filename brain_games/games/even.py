"""Brain-even game"""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_round():
    min_number = 0
    max_number = 99
    question = randint(min_number, max_number)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
