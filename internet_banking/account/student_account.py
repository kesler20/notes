
class StudentAccount():

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    def withdraw_funds(self, amount):
        self.amount -= amount

    def add_funds(self, amount):
        self.amount += amount

    def check_balance(self):
        return self.amount
