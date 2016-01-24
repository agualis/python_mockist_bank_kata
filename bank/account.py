from bank.exceptions import UnsupportedOperationException


class Account():
    def deposit(self, amount):
        raise UnsupportedOperationException()

    def withdraw(self, amount):
        raise UnsupportedOperationException()

    def print_statement(self):
        raise UnsupportedOperationException()
