class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} | Price: ₹{self.price}"

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def __str__(self):
        return super().__str__() + f" | Warranty: {self.warranty} years"

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return super().__str__() + f" | Size: {self.size}"

e = Electronics("Laptop", 75000, 2)
c = Clothing("T-Shirt", 499, "L")
print(e)
print(c)