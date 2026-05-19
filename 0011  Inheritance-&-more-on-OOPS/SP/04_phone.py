class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self, number):
        print(f"{self.brand} calling {number}...")

class Smartphone(Phone):
    def browse_internet(self):
        print(f"{self.brand} browsing internet...")

    def take_photo(self):
        print(f"{self.brand} clicked a photo!")

sp = Smartphone("Redmi")
sp.call("9876543210")
sp.browse_internet()
sp.take_photo()