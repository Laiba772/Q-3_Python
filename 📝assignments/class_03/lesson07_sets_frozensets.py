
# -------------------------
# The Set Data Type
# -------------------------

# Creating a set (unordered collection of unique items)
my_set = {1, 2, 3, 3, 4}
print("Set (duplicates removed):", my_set)  # Output: {1, 2, 3, 4}

# Sets are unordered - no indexing, so this will error:
# print(my_set[0])  # ❌ TypeError: 'set' object is not subscriptable

# -------------------------
# Use difference_update() method to remove multiple elements at once
# -------------------------
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4}

print("Before difference_update:", set_a)
set_a.difference_update(set_b)
print("After difference_update (removed 2 and 4):", set_a)

# -------------------------
# Union using union() and | operator
# -------------------------
set_x = {1, 2, 3}
set_y = {3, 4, 5}

union1 = set_x.union(set_y)
union2 = set_x | set_y

print("Union using union():", union1)
print("Union using | operator:", union2)

# -------------------------
# Unique elements automatically handled in sets
# -------------------------
set_dup = {1, 2, 2, 3, 3, 3}
print("Unique elements only:", set_dup)

# -------------------------
# discard() and remove() methods
# -------------------------
my_set = {1, 2, 3}

my_set.discard(2)   # Removes 2, no error if element not present
print("After discard(2):", my_set)

my_set.remove(3)    # Removes 3, raises KeyError if element not present
print("After remove(3):", my_set)

# my_set.remove(4)  # ❌ KeyError if uncommented

# -------------------------
# The inner working of SET (Advanced)
# -------------------------
# Sets use hashing internally to store elements uniquely.
# Elements must be hashable (immutable types like int, str, tuple).

# -------------------------
# Rehashing and Changing Order
# -------------------------
# Sets are unordered and can change order after insertion or deletion.
s = {1, 2, 3}
print("Original set:", s)
s.add(4)
print("Set after adding 4:", s)

s.remove(2)
print("Set after removing 2:", s)

# The order may appear random and can change between runs.

# -------------------------
# The Frozenset (Immutable Set)
# -------------------------
frozen = frozenset([1, 2, 3, 3, 4])
print("Frozenset (immutable):", frozen)

# frozen.add(5)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'

# -------------------------
# Set Methods Examples
# -------------------------
a = {1, 2, 3}
b = {3, 4, 5}

print("a.intersection(b):", a.intersection(b))
print("a.difference(b):", a.difference(b))
print("a.symmetric_difference(b):", a.symmetric_difference(b))
print("a.isdisjoint(b):", a.isdisjoint(b))
print("a.issubset({1,2,3,4}):", a.issubset({1,2,3,4}))
print("a.issuperset({1,2}):", a.issuperset({1,2}))

# -------------------------
# Frozenset Methods Examples
# -------------------------
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print("fs1.union(fs2):", fs1.union(fs2))
print("fs1.intersection(fs2):", fs1.intersection(fs2))
print("fs1.difference(fs2):", fs1.difference(fs2))
print("fs1.isdisjoint(fs2):", fs1.isdisjoint(fs2))
print("fs1.issubset(fs2):", fs1.issubset(fs2))
print("fs1.issuperset(fs2):", fs1.issuperset(fs2))
