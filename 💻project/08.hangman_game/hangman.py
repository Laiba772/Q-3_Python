import random

# List of words to choose from.
words_list = ['python', 'java', 'javascript', 'ruby', 'c#', 'cplusplus', 'assembly', 'perl', 'go', 'swift']

word = random.choice(words_list)
guessed_letters = []
attempts = 6

displayed_word = "_ " * len(word)
print(f'Welcome to Hangman! The word has {len(word)} letters.')
print(displayed_word)

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Write one alphabet only!")
        continue
    
    if guess in guessed_letters:
        print(f'You have already guessed {guess}. Try again.')
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print(f'Good job! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word.')
        attempts -= 1
        print(f'Attempts left: {attempts}')
    
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print("Congratulations! You've guessed the word.")
        break

else:
    print("Sorry, you've run out of attempts. The word was:", word)
