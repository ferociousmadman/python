# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
# Creates a Water_bill class. This class is a derived class of the
# Utility_bill class. It has an additional protected instance
# variable to store number of gallons of water used. Defines a
# calculate_charge method, which asks the user to enter number of
# gallons of water used and uses it to calculate total charge.
# Customers pay $0.005 per gallon for the first 6000 gallons, and
# $0.007 per gallon after the first 6000 gallons. Defines a
# display_bill method to display customer’s name, address, number
# of gallons of water used and total charge. Includes basic error
# handling in the error_check() function.
# -----------------------------------------------------------------

from Utility_bill import Utility_bill


class Water_bill:

    def __init__(self, name, address, total):

        super().__init__()
        self._num_gallons_used = 0.0
        self._name = name
        self._address = address
        self._total = total

    def calculate_charge(self):
        self._num_gallons_used = error_check(self._num_gallons_used)

        if self._num_gallons_used <= 6000:
            self._total = self._num_gallons_used * 0.005
        elif self._num_gallons_used > 6000:
            self._total = (6000 * 0.005) + ((self._num_gallons_used - 6000) * 0.007)

    def display_bill(self):
        print('\nWater Bill')
        print('Name:', self._name)
        print('Address:', self._address)
        print('Gallons used:', self._num_gallons_used)
        print('Please pay this amount', self._total)

   
def error_check(_num_gallons_used):
    while True:
        try:
            _num_gallons_used = input("How many gallons of water were used? ")
            _num_gallons_used = float(_num_gallons_used)
            if float(_num_gallons_used) >= 0:
                break
            else:
                print("Please enter a positive decimal or integer! ")
        except ValueError:
            print("Please enter a positive decimal or integer! ")
    return _num_gallons_used
