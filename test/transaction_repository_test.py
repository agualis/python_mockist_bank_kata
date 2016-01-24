from unittest import TestCase
from hamcrest import assert_that, equal_to

from bank.transaction_repository import TransactionRepository
from bank.transaction import Transaction
from mockito import verify, mock

def aTransaction(amount):
    return Transaction(100)


class AccountTest(TestCase):
    def setUp(self):
        self.transaction_repository = TransactionRepository()

    def test_account_should_store_a_deposit_transaction(self):
        self.transaction_repository.store(100)

        assert_that(self.transaction_repository.transactions(), equal_to([aTransaction(100)]))


