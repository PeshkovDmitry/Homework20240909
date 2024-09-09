import unittest
from Package01.BankAccount import BankAccount
from Package01.InsufficientFundsError import InsufficientFundsError


class TestBankAccount(unittest.TestCase):

    def test_constructor(self):
        bank_account = BankAccount(100)
        self.assertEqual(bank_account.get_balance(), 100, "Конструктор не создает баланс")

    def test_default_constructor(self):
        bank_account = BankAccount()
        self.assertEqual(bank_account.get_balance(), 0, "Конструктор по умолчанию создает ненулевой баланс")

    def test_deposit(self):
        bank_account = BankAccount(100)
        bank_account.deposit(50)
        self.assertEqual(bank_account.get_balance(), 150, "Деньги на депозит не кладуться")

    def test_withdraw(self):
        bank_account = BankAccount(100)
        bank_account.withdraw(50)
        self.assertEqual(bank_account.get_balance(), 50, "Деньги с депозита не снимаются")

    def test_withdraw_with_error(self):
        bank_account = BankAccount(100)
        self.assertRaises(InsufficientFundsError, bank_account.withdraw, 150)



if __name__ == "__main__":
    unittest.main()
