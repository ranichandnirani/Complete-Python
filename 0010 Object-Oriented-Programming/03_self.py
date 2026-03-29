class Employee:
    salary = 20000
    language = "Python"

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

priya = Employee()
priya.language = "React" #  Instance attributes, take preference over class attributes during assignment & retrieval.
# print(priya.language)

priya.getInfo()