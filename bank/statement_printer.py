STATEMENTS_HEADER = 'DATE | AMOUNT | BALANCE'


class StatementPrinter:
    def __init__(self, console):
        self.console = console
        self.running_balance = 0

    def print_transactions(self, transactions):
        self.console.print_line(STATEMENTS_HEADER)

        lines = [self.statement_line(transaction) for transaction in transactions]
        for line in reversed(lines):
            self.console.print_line(line)

    def statement_line(self, transaction):
        self.running_balance += transaction.amount
        return "%s | %.2f | %.2f" % (transaction.date, transaction.amount, self.running_balance)
