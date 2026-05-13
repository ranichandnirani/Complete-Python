# All Operators 

x = 10
y = 10
z = x

print(x is y)       # True  (small integers cached)
print(x is z)       # True  (same object)
print(x is not y)   # False
print(x is not z)   # False