import random  # Importing the random module to generate a random number.

# Displaying the welcome message to the user.
print("🎉 Welcome to the Number Guessing Game! 🎉")
print("I'm thinking of a number between 30 and 80. Try to guess it!\n")

# Generating a random number between 30 and 80.
random_number = random.randint(30, 80)

# Starting an infinite loop to keep asking for user guesses.
while True:
    try:
        # Taking user input and converting it to an integer.
        user_guess = int(input("Enter your guess: "))
        
        # Checking if the user's guess is lower than the random number.
        if user_guess < random_number:
            print("📉 Too low! Try again.")
        
        # Checking if the user's guess is higher than the random number.
        elif user_guess > random_number:
            print("📈 Too high! Try again.")
        
        # If the guess is correct, display a success message and break the loop.
        else:
            print("🎊 Congratulations! You guessed the correct number! 🎊")
            break  # Exiting the loop when the user guesses correctly.
    
    # Handling cases where the user enters invalid input (non-numeric values).
    except ValueError:
        print("⚠️ Invalid input! Please enter a number between 30 and 80.")

