# Basic Operations

s = "Hello, World!"

print(len(s))           # 13 – length of string
print(s.upper())        # "HELLO, WORLD!" – convert to uppercase
print(s.lower())        # "hello, world!" – convert to lowercase
print(s.title())        # "Hello, World!" – capitalize each word
print(s.swapcase())     # "hELLO, wORLD!" – swap upper/lower case

# Search & Check

print(s.find("World"))       # 7  – index of first occurrence (-1 if not found)
print(s.index("World"))      # 7  – like find() but raises error if not found
print(s.count("l"))          # 3  – count occurrences
print(s.startswith("Hello")) # True
print(s.endswith("!"))       # True
"Hello" in s          # True – membership check


print(s.replace("World", "Python"))

# Split & Join

print(s.split(", "))         # ['Hello', 'World!']
print(s.split())             # splits on whitespace by default
print(s.splitlines())        # splits on newlines
", ".join(["a","b","c"])  # "a, b, c"

# Validate (return True/False)

print("hello".isalpha())    # True  – only letters
print("123".isdigit())      # True  – only digits
print("abc123".isalnum())   # True  – letters or digits
print("  ".isspace())       # True  – only whitespace
print("Hello".istitle())    # True  – title cased
print("HELLO".isupper())    # True
print("hello".islower())    # True

print(s)