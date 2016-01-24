STATEMENTS_HEADER = 'DATE | AMOUNT | BALANCE'


class StatementPrinter():
    def __init__(self, console):
        self.console = console

    def print_transactions(self, transactions):
        self.console.print_line(STATEMENTS_HEADER)
