class Student:
    # name = "Chandni" # class attribute
    # rollno = 252222
    salary = 20000
    language = "Python"

s1 = Student()
s1.name = "Priya" # instance attribute
print(s1.language)

s2 = Student()
s2.name = "Ritik"
print(s2.name, s2.salary, s2.language)