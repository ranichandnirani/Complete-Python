class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

d = Dog("Bruno", 3, "Labrador")
d.display()