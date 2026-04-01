from random import randint

# 6. Can you change the self-parameter inside a class to something else (say “chandni”). Try changing self to “slf” or “harry” and see the effects


class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(chandni, fro, to):
        print(f"Ticket is booked in the no: {chandni.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Ticket no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in the no: {self.trainNo} from {fro} to {to} is {randint(202503, 305127)}")

t = Train(214563)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
