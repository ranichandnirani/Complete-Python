# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 3

o = Demo()
print(o.a)# print the class attribute bcz instance attribute is not present.

o.a = 0 # instance attribute
print(o.a)# print the instance attribute bcz instance attribute is present.