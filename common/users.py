""" Module to represent a user, with all its attributes """

from .bill import Bill

class Customer:
    """ Class to represent a user, with name and email """

    def __init__(self, name: str, days_in_house: int, email: str=None) -> None:
        self.name = name
        self.days_in_house = days_in_house
        self.email = email
    
    def pay(self, bill: Bill, customer: "Customer") -> None:
        """ Method to calculate the amount to pay """
        weight = self.days_in_house / (self.days_in_house + customer.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
