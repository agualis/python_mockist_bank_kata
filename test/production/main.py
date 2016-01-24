from bank.account import Account
from bank.clock import Clock
from bank.console import Console
from bank.statement_printer import StatementPrinter
from bank.transaction_repository import TransactionRepository


def main():
    account = Account(TransactionRepository(Clock()), StatementPrinter(Console()))
    account.deposit(1000)
    account.withdraw(100)
    account.deposit(500)
    account.print_statement()

if __name__ == "__main__":
    main()