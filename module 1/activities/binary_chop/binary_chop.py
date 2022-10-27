import random
target: int = random.randint(1,100)
while True:
  guess = int(input("guess a number between 1 and 100: "))
  if guess == target:
    print ("You got it!!")
    break
  elif guess < target:
    print ("Sorry, too low -- try a higher number")
  elif guess > target:
    print ("Sorry, too high -- try a lower number")
