class InsufficientFunds(Exception):
    pass


class Wallet:
    def __init__(self, amount=0):
        self.balance = amount

    def add_cash(self, amount):
        self.balance += amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientFunds("Not enough funds")
        self.balance -= amount
