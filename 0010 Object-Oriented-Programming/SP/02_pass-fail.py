# Q2. Student Pass/Fail

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 33

s1 = Student("Chandni", 85)
s2 = Student("Rahul",   25)
print(f"{s1.name}: {'Pass' if s1.is_pass() else 'Fail'}")
print(f"{s2.name}: {'Pass' if s2.is_pass() else 'Fail'}")