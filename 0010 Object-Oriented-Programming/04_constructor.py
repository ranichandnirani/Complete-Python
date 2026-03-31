class Employee:
    salary = 20000
    language = "Python"

    def __init__(self): # dunder method which is automatically called
        print("I am creating an Object")

    def getInfo(self): # method
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello from Priyuu!")

priya = Employee()
priya.name = "Priya"

print(priya.name, priya.salary)