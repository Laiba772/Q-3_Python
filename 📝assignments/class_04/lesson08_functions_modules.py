
# Lesson 08: Control Modules & Functions

# 1. Basic Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Laiba"))




# 2. Function with default argument
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Ali")





# 3. Keyword Arguments
def user_info(name, age):
    print(f"Name: {name}, Age: {age}")

user_info(age=20, name="Laiba")





# 4. Return multiple values
def calc(a, b):
    return a + b, a * b

add, mul = calc(3, 4)
print("Addition:", add)
print("Multiplication:", mul)




# 5. Creating and importing a module (Demonstration)
# This would go in another file in real use
def square(n):
    return n ** 2

print("Square of 5 is:", square(5))





# 6. Import built-in module
import math
print("Square root of 25:", math.sqrt(25))
