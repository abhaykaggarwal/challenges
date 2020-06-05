"""Pomodoro Timer for 100 Days of Python on June 4th, 2020
    Instructions at https://codechalleng.es/challenges/52/
    CREDITS:
    1. https://stackabuse.com/getting-user-input-in-python/"""

from datetime import timedelta
import time
import sys

timer_dur = None
break_dur = None
num_iter = None

def timer(min_dur):

    secs_dur = min_dur * 60
    while secs_dur >= 0:
        print("Pomodoro Time Remaining: {}\r".format(timedelta(seconds=secs_dur)), end="")
        time.sleep(1)
        secs_dur = secs_dur - 1
    print("--TIME IS UP, TAKE A BREAK--")

def break_timer(b_dur):

    secs_dur = b_dur * 60
    while secs_dur >= 0:
        print("Break Time Remaining: {}\r".format(timedelta(seconds=secs_dur)), end="")
        time.sleep(1)
        secs_dur = secs_dur - 1
    print("--BREAK TIME IS UP, POMODORO WILL RESTART--")


def main():
    use_iter = num_iter
    while use_iter > 1:
        timer(timer_dur)
        time.sleep(2)
        break_timer(break_dur)
        time.sleep(2)
        use_iter = use_iter - 1
    timer(timer_dur)
    time.sleep(1)
    print("--TIMER AND BREAKS NOW OVER, ENJOY THE REST OF YOUR DAY--")
    sys.exit(0)



if __name__ == "__main__":

    print("--WELCOME TO THE POMODORO TIMER--")
    timer_string = input('Duration for the timer in minutes:')
    try:
        timer_dur = int(timer_string)
    except ValueError:
        print(
            "This is not a valid number. It isn't a number at all! This is a string, go and try again. "
            + "Better luck next time!")
        print("RESTART PROGRAM")
        sys.exit(1)

    break_string = input('Duration for the break in minutes:')
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

    print("--TIMER WILL START NOW--")
    main()

