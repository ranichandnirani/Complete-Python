class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

class CEO(Manager):
    def __init__(self, name, salary, team_size, company):
        super().__init__(name, salary, team_size)
        self.company = company

    def display(self):
        print(f"CEO: {self.name}")
        print(f"Company: {self.company}")
        print(f"Team Size: {self.team_size}")
        print(f"Salary: ₹{self.salary}")

ceo = CEO("Ratan Tata", 1000000, 500, "Tata Motors")
ceo.display()