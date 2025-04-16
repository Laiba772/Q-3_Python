# project 2 : Guess the Number Game by Computer.

# 1 to 50 numbers.
        
import random

def guess_the_number():
    number = random.randint(1, 50)
    guesses_left = 7

    # welcome message.

    print("Welcome to the Guess the Number Game by Computer!")
    print("I'm thinking of a number between 1 and 50.")

   # loop generated.

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # guess the secret number.

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.") 
            return

        guesses_left -= 1

        # all the guesses  are finished.

    print(f"\nYou've run out of guesses. The correct number was {number}.")

guess_the_number()
