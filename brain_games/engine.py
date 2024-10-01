import prompt

MAX_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    current_round = 1
    while current_round <= MAX_ROUNDS:
        question, correct_answer = game.get_game_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print(f'"{user_answer}" is is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
