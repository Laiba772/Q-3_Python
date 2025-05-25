from models import User, CheerfulCompanion, CalmCompanion, Session

# Step 1: Create user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
user = User(name, age, email)

# Step 2: Choose your companion
print("\nChoose your virtual companion:")
print("1. Cheerful")
print("2. Calm")
choice = input("Enter 1 or 2: ")

if choice == "1":
    companion = CheerfulCompanion("Sunny")
else:
    companion = CalmCompanion("Luna")

# Step 3: Start a session
print("\nLet's log your mood!")
mood = input("How are you feeling today? ")
note = input("Anything you'd like to share? ")

session = Session(user, companion)
session.start(mood, note)

# Step 4: View mood logs
print("\nYour mood logs:")
for log in user.mood_logs:
    print(f"{log.date.strftime('%Y-%m-%d %H:%M')} - Mood: {log.mood}, Note: {log.note}")
