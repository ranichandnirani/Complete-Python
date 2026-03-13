#  2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Priya", "Soham", "Sachin", "Roshan", "Ritik"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

