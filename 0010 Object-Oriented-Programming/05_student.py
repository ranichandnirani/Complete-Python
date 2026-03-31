class Student:
    def __init__(self, name, rollno, email):
        self.name = name
        self.rollno = rollno
        self.email = email

obj = Student("Gauri", 252222, "abc@example.com")

print(obj.name, obj.rollno, obj.email)