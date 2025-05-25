
# -------------------------
# 1. Lists in Python
# -------------------------

# Accessing List Elements
fruits = ['apple', 'banana', 'cherry']
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying Lists
fruits[1] = 'blueberry'
print("Modified list:", fruits)

# List Slicing
print("First two fruits:", fruits[:2])
print("Fruits from index 1:", fruits[1:])

# -------------------------
# 2. Common List Methods
# -------------------------

# Removing elements
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print("After remove:", numbers)

# pop() method
popped_item = numbers.pop()
print("Popped item:", popped_item)
print("List after pop:", numbers)

# Sorting a list

# 1. Default Sorting (Ascending Order)
names = ["Zain", "Ali", "Sara"]
names.sort()
print("Sorted names:", names)

# 2. Descending Order
names.sort(reverse=True)
print("Descending sort:", names)

# 3. Sorting by String Length
words = ['apple', 'kiwi', 'banana']
words.sort(key=len)
print("Sorted by length:", words)

# 4. Sorting by Last Character
words.sort(key=lambda word: word[-1])
print("Sorted by last character:", words)

# 5. Reverse Sorting
nums = [5, 2, 9, 1]
nums.reverse()
print("Reversed list:", nums)

# -------------------------
# 3. Iterating Over Lists
# -------------------------

colors = ['red', 'green', 'blue']
for color in colors:
    print("Color:", color)

# -------------------------
# 4. Tuples in Python
# -------------------------

coordinates: tuple[int, int] = (10, 20)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Tuples are immutable
# coordinates[0] = 5  # ❌ Error

# -------------------------
# Python is a Type Hint Language
# -------------------------

def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("Laiba")

# -------------------------
# 5. Dictionaries in Python
# -------------------------

# 2. Creating a Dictionary
student = {
    "name": "Laiba",
    "age": 21,
    "grade": "A"
}

# 3. Accessing Values
print("Name:", student["name"])
print("Age:", student.get("age"))

# 4. Modifying a Dictionary
student["grade"] = "A+"
print("Updated grade:", student["grade"])

# 5. Deleting Item
del student["age"]
print("After deleting age:", student)

# 6. Dictionary Methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
