from random import randint # import the radnint function from the random module
target = randint(1,100) # pick a number between 1 and 100, INCLUDING 100 unlike with range(1,100)
while True:
    guess = int(input('Guess a number between 1 and 100')) # integer version of what you input
    # code goes here