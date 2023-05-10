""" This is the main file of the project. """

from .generators.pdf_generator import PdfReport
from .common.users import Customer
from .common.bill import Bill


person_1 = Customer(name="Person 1", email="", days_in_house=33)
person_2 = Customer(name="Person 2", email="", days_in_house=232)

bill = Bill(amount=120, period="March 2021")




