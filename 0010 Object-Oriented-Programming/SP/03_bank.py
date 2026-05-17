# Q3. Bank Account

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)