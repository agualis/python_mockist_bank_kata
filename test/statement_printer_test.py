from unittest import TestCase

from mockito import verify, mock

from bank.statement_printer import StatementPrinter, STATEMENTS_HEADER
from bank.transaction import Transaction


class StatementPrinterTest(TestCase):
    def test_print_transactions(self):
        console = mock()
        statement_printer = StatementPrinter(console)

        statement_printer.print_transactions([
            a_transaction(1000, '01/04/2015'),
            a_transaction(-100, '02/04/2015'),
            a_transaction(500, '10/04/2015')])

        verify(console).print_line(STATEMENTS_HEADER)
        verify(console).print_line('10/04/2015 | 500.00 | 1400.00')
        verify(console).print_line('02/04/2015 | -100.00 | 900.00')
        verify(console).print_line('01/04/2015 | 1000.00 | 1000.00')


def a_transaction(amount, today):
    return Transaction(amount, today)