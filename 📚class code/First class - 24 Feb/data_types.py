
# 1 Numeric data types.

#a.integar (int)
# Whole numbers, positive or negative, without decimals.

num_init:int = 42
print(type(num_init),"num_init=", num_init)

#b.floating point (float)
# number with decimal point.

# num_float:float = 3.142
num_float:float = .142

print(type(num_float), "num_float=",num_float)

# c. Complex (complex)
# Numbers with a real and imaginary part.

num_complex : complex = 2+3j
print(type(num_complex), "num_complex=",num_complex)

# 2. Boolean (bool)
# Represents True or False.

is_python_fun: bool = True
is_python_boring: bool = False
print(type(is_python_fun), "is_python_fun=",is_python_fun)
print(type(is_python_boring), "is_python_boring=",is_python_boring)


# 3. Sequence Types
# These store multiple items in an ordered way.

# a. String (str)
# A sequence of characters enclosed in quotes.


text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>


# Key Takeaways
# Double Quotes ("): Use when the string contains single quotes.
# Single Quotes ('): Use when the string contains double quotes.
# Triple Quotes (''' or """): Use for multi-line strings or docstrings.


# b. List (list)
# An ordered, mutable collection.


my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead


# c. Tuple (tuple)
# An ordered, immutable collection.



my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  # <class 'tuple'>


# d. Range (range)
# Represents a sequence of numbers.


num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>

for i in range(1, 10, 2): # we will study loops indepth in classes ahead
  print(i)
1
3
5
7
9



