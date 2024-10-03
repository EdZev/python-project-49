"""Brain-progression game"""

from random import randint

DESCRIPTION = 'What number is missing in the progression?.'


def get_progression(
    progression_length_range,
    progression_step_range,
    progression_range
):
    progression_length = randint(*progression_length_range)
    progression_step = randint(*progression_step_range)
    range_start, range_end = progression_range
    end_progression_range = range_end - progression_length * progression_step
    start_progression = randint(range_start, end_progression_range)

    progression = []
    for i in range(start_progression, range_end, progression_step):
        if progression_length > 0:
            progression.append(i)
            progression_length -= 1
        else:
            break

    return progression


def get_game_round():
    progression = get_progression(
        progression_length_range=[5, 10],
        progression_step_range=[1, 10],
        progression_range=[0, 100],
    )
    hidden_index = randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join([str(i) for i in progression])
    return question, str(correct_answer)
