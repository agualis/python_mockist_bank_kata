from unittest import TestCase

from hamcrest import *

from bank.account import Account
from mockito import verify, mock


class Console():
    def print_line(self, text):
        print text


class PrintStatementFeature(TestCase):
    def test_print_statement_containing_all_transactions(self):
        console = mock()

        account = Account()
        account.deposit(1000)
        account.withdraw(100)
        account.deposit(500)

        verify(console).print_line('DATE | AMOUNT | BALANCE')
        verify(console).print_line('10/04/2015 | 500.00 | 1400.00')
        verify(console).print_line('02/04/2015 | -100.00 | 900.00')
        verify(console).print_line('01/04/2015 | 1000.00 | 1000.00')
