from random import randint

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in the no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Ticket no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in the no: {self.trainNo} from {fro} to {to} is {randint(202503, 305127)}")

t = Train(214563)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
