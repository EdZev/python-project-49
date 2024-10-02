"""Brain-even game"""

from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_game_round():
    min_number = 0
    max_number = 99
    first_operand = randint(min_number, max_number)
    second_operand = randint(min_number, max_number)
    correct_answer = gcd(first_operand, second_operand)
    question = f'{first_operand} {second_operand}'
    return question, str(correct_answer)
