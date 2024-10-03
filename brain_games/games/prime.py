"""Brain-prime game"""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return 'no'
    for i in range(2, num - 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def get_game_round():
    min_number = 1
    max_number = 99
    question = randint(min_number, max_number)
    correct_answer = is_prime(question)
    return question, correct_answer
