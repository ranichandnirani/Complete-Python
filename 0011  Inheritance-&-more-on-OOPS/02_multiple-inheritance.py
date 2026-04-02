class Employee:  # Base class
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all language: {self.language}")


class Programmer(Employee, Coder): # Derived class or child class
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.language}")

a=Employee()
b=Programmer()

b.show()
b.printLanguages()
b.showLanguage()