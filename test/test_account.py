from unittest import TestCase

from bank.account import Account
from mockito import verify, mock


class AccountTest(TestCase):
    def setUp(self):
        self.transaction_repository = mock()
        self.account = Account(self.transaction_repository, None)

    def test_account_should_store_a_deposit_transaction(self):
        self.account.deposit(100)

        verify(self.transaction_repository).store(100)

    def test_account_should_store_a_withdraw_transaction(self):
        self.account.withdraw(50)

        verify(self.transaction_repository).store(-50)

