# 3. Find Largest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is Greates.")

elif b >= a and b >= c:
    print("B is Greatest.")

else:
    print("C is Greatest.")