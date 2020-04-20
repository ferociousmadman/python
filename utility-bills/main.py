# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
# In the main module, asks user to enter name and address. Asks the
# user to choose either water bill or electricity bill. Creates an
# object and calls its calculate_charge method to calculate total
# charge. Calls the display_bill method to display the bill.
# Includes basic error handling in the error_check() function.
# -----------------------------------------------------------------

from Utility_bill import Utility_bill
from Water_bill import Water_bill
from Electricity_bill import Electricity_bill


def main():
    name = input('Enter name: ')
    address = input('Enter address: ')
    usr_input = input('Enter 1 for water bill, 2 for electricity bill: ')
    usr_input = error_check(usr_input)
    total = 0.0
    water = Water_bill(name, address, total)
    electric = Electricity_bill(name, address, total)

    if usr_input == '1':
        water.calculate_charge()
        water.display_bill()

    elif usr_input == '2':
        electric.calculate_charge()
        electric.display_bill()


def error_check(usr_input):
    while usr_input != '2' and usr_input != '1':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for water bill, 2 for electricity bill: ')
    return usr_input


main()
