from bank.transaction import Transaction


class TransactionRepository:
    def __init__(self, clock):
        self.clock = clock
        self._transactions = []

    def store(self, amount):
        self._transactions.append(Transaction(amount, self.clock.date_as_string()))

    def all_transactions(self):
        #TODO: better doing it INMUTABLE
        return self._transactions
