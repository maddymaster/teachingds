import random

comGuess = random.randint(0,100)
while True:
    userGuess = int(input("Guess a number between 0 - 100: "))
    if userGuess > comGuess:
        print("Guess a lower number")
    elif userGuess < comGuess:
        print("Guess a higher number")
    else:
        print("Congrats you have guessed the correct number")
        break

