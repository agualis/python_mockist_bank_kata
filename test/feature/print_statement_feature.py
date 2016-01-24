from unittest import TestCase

from mockito import mock, inorder

from bank.account import Account
from bank.transaction_repository import TransactionRepository
from bank.statement_printer import StatementPrinter


class PrintStatementFeature(TestCase):
    def test_print_statement_containing_all_transactions(self):
        console = mock()

        account = Account(TransactionRepository(), StatementPrinter())
        account.deposit(1000)
        account.withdraw(100)
        account.deposit(500)

        account.print_statement()

        inorder.verify(console).print_line('DATE | AMOUNT | BALANCE')
        inorder.verify(console).print_line('10/04/2015 | 500.00 | 1400.00')
        inorder.verify(console).print_line('02/04/2015 | -100.00 | 900.00')
        inorder.verify(console).print_line('01/04/2015 | 1000.00 | 1000.00')
