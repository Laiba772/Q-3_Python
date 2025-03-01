# MadLib Game in Python

# User Input
name = input("Enter your name: ")
gender = input("Choose your Gender (girl, boy): ").strip().lower()
programming_language = input("Enter your favorite programming language (Python, Next.js, Java, C++, JavaScript, etc.): ")
mentor = input("Enter your mentor's name: ")
location = input("Enter your location (e.g., Governor House, Lyari, Shahrah-e-Faisal): ")

# Adjusting Pronouns Based on Gender
if gender == "boy":
    pronoun = "he"
    possessive_pronoun = "his"
else:
    pronoun = "she"
    possessive_pronoun = "her"

# MadLib Story
print("\n✨ Here is your customized MadLib Story! ✨\n")
print(f"Once upon a time, there was a {gender} named {name}.")
print(f"{name} was very curious and always wanted to learn new things.")
print(f"{pronoun.capitalize()} was a brilliant student and always scored well in exams.")
print(f"One day, {name} decided to learn {programming_language} at {location}.")
print(f"{pronoun.capitalize()} was very excited and started exploring {programming_language}.")
print(f"Luckily, {name} found an amazing mentor named {mentor}, who was an expert in {programming_language}.")
print(f"With {mentor}'s guidance, {name} mastered {programming_language} and built an incredible project.")
print(f"{pronoun.capitalize()} was thrilled and shared {possessive_pronoun} work with {mentor}.")
print(f"{mentor} was extremely proud and decided to surprise {name} with a special gift.")
print(f"The gift was an advanced {programming_language} course to help {name} become even better!")

print("\n🎉 The End! Keep Learning & Keep Coding! 🚀\n")
