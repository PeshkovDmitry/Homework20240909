from Package01.InsufficientFundsError import InsufficientFundsError


class BankAccount:

    def __init__(self, account: float = 0):
        if account > 0:
            self.account = account
        else:
            self.account = 0

    def deposit(self, amount: float):
        self.account += amount

    def withdraw(self, amount):
        if self.account > amount:
            self.account -= amount
        else:
            raise InsufficientFundsError

    def get_balance(self) -> float:
        return self.account
