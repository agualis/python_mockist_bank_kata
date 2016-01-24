from unittest import TestCase

from hamcrest import assert_that, contains
from mockito import mock, when

from bank.transaction_repository import TransactionRepository
from bank.transaction import Transaction


class AccountTest(TestCase):
    def setUp(self):
        self.clock = mock()
        self.transaction_repository = TransactionRepository(self.clock)

    def test_account_should_store_a_deposit_transaction(self):
        when(self.clock).date_as_string().thenReturn('01/04/2015').thenReturn('02/04/2015').thenReturn('10/04/2015')

        self.transaction_repository.store(100)
        self.transaction_repository.store(-50)
        self.transaction_repository.store(20)

        assert_that(self.transaction_repository.all_transactions(), contains(
            a_transaction(100, '01/04/2015'),
            a_transaction(-50, '02/04/2015'),
            a_transaction(20, '10/04/2015')))


def a_transaction(amount, today):
    return Transaction(amount, today)
