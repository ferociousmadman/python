# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
# Creates a Utility_bill class. This class has two protected instance
# variables: name and address. The __init__ method takes customer’s
# name and address as two arguments and stores them in the instance
# variables. Adds another protected instance variable total and
# initializes it to 0. Defines two abstract methods calculate_charge
# and display_bill. These abstract methods have no real code.
# There is only one statement to raise a NotImplementedError
# exception.
# -----------------------------------------------------------------


class Utility_bill:

    def __int__(self, name, address):
        self._name = name
        self._address = address
        self._total = 0.0

    def calculate_charge(self):
        pass

    def display_bill(self):
        pass
