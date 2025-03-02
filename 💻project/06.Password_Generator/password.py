#  project 6  password generator in python.
import random
import string

def generate_password(length=12):
    """Generate a strong random password with given length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 for better security.")

    # Ensuring at least one character from each category
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]
    
    # Fill the remaining password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# User input with validation
while True:
    try:
        length = int(input("Enter the length of your desired password: "))
        if length >= 4:
            break
        print("Password length must be at least 4.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Generate and display password
password = generate_password(length)
print(f"Your generated password is: {password}")
