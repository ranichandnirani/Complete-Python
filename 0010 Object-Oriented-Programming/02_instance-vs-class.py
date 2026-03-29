class Employee:
    salary = 20000
    language = "Python"

priya = Employee()
priya.language = "React" #  Instance attributes, take preference over class attributes during assignment & retrieval.
print(priya.language)

