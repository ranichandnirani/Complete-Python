class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def describe(self):
        super().describe()
        print(f"Doors: {self.num_doors}")

c = Car("Toyota", 180, 4)
c.describe()