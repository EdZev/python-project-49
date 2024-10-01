"""Brain-even game"""

from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def get_game_round():
    min_number = 0
    max_number = 99
    first_operand = randint(min_number, max_number)
    second_operand = randint(min_number, max_number)
    operators = [
        [add, '+'],
        [sub, '-'],
        [mul, '*'],
    ]
    operation, designation = choice(operators)
    correct_answer = operation(first_operand, second_operand)
    question = f'{first_operand} {designation} {second_operand}'
    return question, str(correct_answer)
