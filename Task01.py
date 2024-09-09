import pytest
from Package01.BankAccount import BankAccount
from Package01.InsufficientFundsError import InsufficientFundsError


def test_constructor():
    bank_account = BankAccount(100)
    assert bank_account.get_balance() == 100, "Конструктор не создает баланс"


def test_default_constructor():
    bank_account = BankAccount()
    assert bank_account.get_balance() == 0, "Конструктор по умолчанию создает ненулевой баланс"


def test_deposit():
    bank_account = BankAccount(100)
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150, "Деньги на депозит не кладуться"


def test_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.get_balance() == 50, "Деньги с депозита не снимаются"


def test_withdraw_with_error():
    bank_account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(150)


if __name__ == "__main__":
    pytest.main(['-v'])
