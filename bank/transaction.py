class Transaction():
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.amount == other.amount