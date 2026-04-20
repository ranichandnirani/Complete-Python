# Raising error 

# We can raise custom exceptions using the ‘raise’ keyword in python.

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not ment to divide number by zero")

else:
    print(f"The division a/b is {a / b}")