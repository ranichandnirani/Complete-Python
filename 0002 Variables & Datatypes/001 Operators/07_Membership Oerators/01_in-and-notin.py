# Works On All Sequences

# String
print("p" in "python")         # True
print("z" not in "python")     # True

# List
print(3 in [1, 2, 3, 4])       # True

# Tuple
print(10 in (10, 20, 30))      # True

# Set
print(5 in {1, 3, 5, 7})       # True

# Dictionary (checks KEYS by default)
print("name" in {"name": "Alice", "age": 25})   # True
print("Alice" in {"name": "Alice", "age": 25})  # False