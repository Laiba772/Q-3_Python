
# ------------------------
# The if Statement
# ------------------------
x = 10
if x > 5:
    print("x is greater than 5")

# ------------------------
# The else Statement
# ------------------------
if x < 5:
    print("x is less than 5")
else:
    print("x is not less than 5")

# ------------------------
# The elif Statement
# ------------------------
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# ------------------------
# Nested if Statements
# ------------------------
age = 20
if age > 10:
    if age < 25:
        print("Age is between 10 and 25")

# ------------------------
# Practical Example 1: Simple Calculator
# ------------------------
a = 5
b = 3
operator = '+'

if operator == '+':
    print("Addition:", a + b)
elif operator == '-':
    print("Subtraction:", a - b)
elif operator == '*':
    print("Multiplication:", a * b)
elif operator == '/':
    print("Division:", a / b)
else:
    print("Invalid operator")

# ------------------------
# Practical Example 2: Grade Checker
# ------------------------
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# ------------------------
# Python match-case Statement (like switch)
# Python 3.10+ only
# ------------------------
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# ------------------------
# The for Loop
# ------------------------
for i in range(5):
    print("i =", i)

# ------------------------
# For loop with else
# ------------------------
for i in range(3):
    print("Looping", i)
else:
    print("Loop finished!")

# ------------------------
# The while loop
# ------------------------
count = 0
while count < 3:
    print("Count is", count)
    count += 1

# ------------------------
# Controlling loop: break and continue
# ------------------------
# break example
for i in range(5):
    if i == 3:
        break
    print("Break Example:", i)

# continue example
for i in range(5):
    if i == 2:
        continue
    print("Continue Example:", i)

# ------------------------
# Nested loops
# ------------------------
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
