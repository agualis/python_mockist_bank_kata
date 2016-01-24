from bank.transaction import Transaction


class TransactionRepository():
    def __init__(self):
        self._transactions = []

    def store(self, amount):
        self._transactions.append(Transaction(amount))

    def all_transactions(self):
        #TODO: better doing it INMUTABLE
        return self._transactions
