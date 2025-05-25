
# Identity Operators.


a = [1, 2]
b = [1, 2]
c = a
print("\nIdentity Operators:")
print("a is c:", a is c)
print("a is b:", a is b)
print("a is not b:", a is not b)


# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators:")
print("a is b:", a is b)          # True (same object)
print("a is c:", a is c)          # False (different object)

print("a is not c:", a is not c)  # True
print("b is not a:", b is not a)  # False
