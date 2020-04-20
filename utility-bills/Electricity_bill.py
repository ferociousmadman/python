# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
# Creates a Electricity_bill class. This class is a derived class of
# the Utility_bill class. It has an additional protected instance
# variable to store kilowatt hours used. Defines a calculate_charge
# method, which asks the user to enter kilowatt hours used and uses
# it to calculate total charge. Customers pay $0.12 per kWh for the
# first 500 kWh, and $0.15 per kwh after the first 500 kWh. Defines
# a display_bill method to display customer’s name, address, number
# of kWh used and total charge. Includes basic error handling in
# the error_check() function.
# -----------------------------------------------------------------

from Utility_bill import Utility_bill


class Electricity_bill:

    def __init__(self, name, address, total):

        super().__init__()
        self._kilowatt_hours_used = 0.0
        self._name = name
        self._address = address
        self._total = total

    def calculate_charge(self):
        self._kilowatt_hours_used = error_check(self._kilowatt_hours_used)

        if self._kilowatt_hours_used <= 500:
            self._total = self._kilowatt_hours_used * 0.12
        elif self._kilowatt_hours_used > 500:
            self._total = (500 * 0.12) + ((self._kilowatt_hours_used - 500) * 0.15)

    def display_bill(self):
        print('\nElectricity Bill')
        print('Name:', self._name)
        print('Address:', self._address)
        print('Kilowatt Hours used:', self._kilowatt_hours_used)
        print('Please pay this amount', self._total)


def error_check(_kilowatt_hours_used):
    while True:
        try:
            _kilowatt_hours_used = input("Enter kilowatt hours used: ")
            _kilowatt_hours_used = float(_kilowatt_hours_used)
            if float(_kilowatt_hours_used) >= 0:
                break
            else:
                print("Please enter a positive decimal or integer! ")
        except ValueError:
            print("Please enter a positive decimal or integer! ")
    return _kilowatt_hours_used
