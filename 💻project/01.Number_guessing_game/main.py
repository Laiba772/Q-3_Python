#  this is a simple number guessing game.
#  the user gets 5 attempts to guess the number between 50 and 100.
#  the user can guess the number only once.


import random
# random is module in python.

print("Welcome to the Number guessing game! \n you get 5 attempts to guess the number between 50 and 100, let's start the game")

number_to_guess = random.randrange(50,100)
# randrange is a function in random module.

chances = 5
# chances is a variable that is used to count the number of chances.

guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
 # while loop is used to repeat the code block until the condition is false.
# guess_counter is a variable that is used to count the number of guesses.



    my_guess = int(input("Please enter your guess:"))

# input is a function that is used to get the input from the user.
# int is a function that is used to convert the input to an integer.


    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you fount it right!! in the {guess_counter} attempt")

        break
     #  break is used to exit the loop.
     # if the guess is correct, the loop will break.
    
    elif guess_counter >= chances and my_guess != number_to_guess:
     #  elif is used to check the condition if the guess is not correct.
    #  guess_counter >= chances is used to check the number of chances.
    #  my_guess != number_to_guess is used to check the guess is not correct.
        print(f" Oops Soory, the number is {number_to_guess} better luck next time")
    #  print is used to print the message.
    #  number_to_guess is the number that the user is trying to guess.
    #  f is used to format the string.
    elif my_guess < number_to_guess:
        print("your guess is very low, try again!")
    elif my_guess > number_to_guess:
        print("your guess is very high, try again!")
