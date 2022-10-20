import random

MAX_GUESSES: int = 7

def try_again() -> bool:
    while True:
        response = int(input('Try again? [1]Yes / [2]No\n'))
        if response == 1 or response == 2:
            break
    if response == 1: 
        return True
    return False

def all_guesses_used(guesses_used, max_guesses = MAX_GUESSES) -> bool:
    if guesses_used > max_guesses:
        return True
    return False

def update_guesses(guesses_used) -> int:
    guesses_used += 1
    return guesses_used

def binary_chop():
    target: int = random.randint(1,100)
    guesses_used: int = 1
    while True:
        guess = int(input('Guess a number between 1 and 100: '))
        match guess:
            case guess if guess > target:
                print ('Sorry, too high')
                guesses_used = update_guesses(guesses_used)
            case guess if guess < target:
                print ('Sorry, too low')
                guesses_used = update_guesses(guesses_used)
            case _:
                print ('You got it!!')
                break
        if all_guesses_used(guesses_used):
            print('Game over!')
            break

if __name__ == '__main__':
    while True:
        binary_chop()
        if not try_again():
            break
