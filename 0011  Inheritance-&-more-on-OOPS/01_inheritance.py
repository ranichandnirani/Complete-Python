class Employee:  # Base class
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and the salary is {self.language} language")

class Programmer(Employee): # Derived class or child class
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a=Employee()
b=Programmer()

print(a.company, b.company)