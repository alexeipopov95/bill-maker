""" Bill schema"""

class Bill:
    """ Class to represent a bill, with amount and currency """

    def __init__(self, amount: float, period: str) -> None:
        self.amount = amount
        self.period = period