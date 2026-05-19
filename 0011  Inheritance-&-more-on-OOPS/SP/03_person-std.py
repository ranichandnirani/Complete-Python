class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        super().display()
        print(f"Marks: {self.marks}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

s = Student("Chandni", 20, 92)
t = Teacher("Mrs. Malik", 35, "Python")
print("--- Student ---")
s.display()
print("--- Teacher ---")
t.display()