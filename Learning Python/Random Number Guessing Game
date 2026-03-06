# Random Number Guessing Game:

import random
num = random.randint(0, 100)
guess = input("Guess: ")
try:
    guess = int(guess)
    while guess!=num:
        if guess>num:
            print(f"Your guess is too big. Hint: You're about {round((guess-num)/10)*10} off.")
        elif guess<num:
            print(f"Your guess is too small. Hint: You're about {round((num-guess)/10)*10} off.")
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Guess should be an integer.")
    print(f"You got it, the number was {num}.")
except ValueError:
    print("Guess should be an integer.")