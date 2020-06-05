"""Pomodoro Timer for 100 Days of Python on June 4th, 2020
    Instructions at https://codechalleng.es/challenges/52/
    CREDITS:
    1. https://stackabuse.com/getting-user-input-in-python/"""

from datetime import datetime
from datetime import timedelta
import sys

timer_dur = None
break_dur = None
num_iter = None


def main():
    print(timer_dur)




if __name__ == "__main__":
    print("--WELCOME TO THE POMODORO TIMER--")

    timer_string = input('Duration for the timer:')
    try:
        timer_dur = int(timer_string)
    except ValueError:
        print(
            "This is not a valid number. It isn't a number at all! This is a string, go and try again. "
            + "Better luck next time!")
        print("RESTART PROGRAM")
        sys.exit(1)

    break_string = input('Duration for the break:')
    try:
        break_dur = int(break_string)
    except ValueError:
        print(
            "This is not a valid number. It isn't a number at all! This is a string, go and try again. "
            + "Better luck next time!")
        print("RESTART PROGRAM")
        sys.exit(1)

    iter_string = input('Iterations of the Timer:')
    try:
        num_iter = int(iter_string)
    except ValueError:
        print(
            "This is not a valid number. It isn't a number at all! This is a string, go and try again. "
            + "Better luck next time!")
        print("RESTART PROGRAM")
        sys.exit(1)

    main()

