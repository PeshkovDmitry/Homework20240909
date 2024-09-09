class InsufficientFundsError(Exception):

    def __str__(self):
        return "Недостаточно средств на счете"

