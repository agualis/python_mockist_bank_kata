from bank.exceptions import UnsupportedOperationException


class Account():
    def __init__(self, transaction_repository, statement_printer):
        self.transaction_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount):
        self.transaction_repository.store(amount)

    def withdraw(self, amount):
        self.transaction_repository.store(-amount)

    def print_statement(self):
        self.statement_printer.print_transactions(self.transaction_repository.all_transactions())
