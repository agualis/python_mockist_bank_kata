from unittest import TestCase

from hamcrest import assert_that, contains

from bank.transaction_repository import TransactionRepository
from bank.transaction import Transaction


class AccountTest(TestCase):
    def setUp(self):
        self.transaction_repository = TransactionRepository()

    def test_account_should_store_a_deposit_transaction(self):
        self.transaction_repository.store(100)
        self.transaction_repository.store(-50)
        self.transaction_repository.store(20)

        assert_that(self.transaction_repository.all_transactions(), contains(
            aTransaction(100),
            aTransaction(-50),
            aTransaction(20)))


def aTransaction(amount):
    return Transaction(amount)
