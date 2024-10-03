#!/usr/bin/env python3
"""Brain-Progression Game start"""

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    run_game(progression)


if __name__ == '__main__':
    main()
