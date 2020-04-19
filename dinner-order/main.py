# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
#
# This program creates the main module for the dinner order program.
# It asks the user to choose either regular or deluxe dinner combo.
# Creates an object and calls its methods to input food items and
# displays the information of the order. NOTE: commas and spaces
# appear as they did in the example.
# -----------------------------------------------------------------


from Dinner_combo import Dinner_combo
from Deluxe_dinner_combo import Deluxe_dinner_combo


def main():
    dinner_order = Dinner_combo()
    dinner_order_with_appetizer = Deluxe_dinner_combo()
    usr_input = input('Enter 1 for dinner combo or 2 for deluxe dinner combo: ')

    usr_input = error_check(usr_input)

    usr_input = int(usr_input)
    if usr_input == 1:
        dinner_order.choose_soup()
        dinner_order.choose_dish()
        dinner_order.displayOrder()
    elif usr_input == 2:
        dinner_order_with_appetizer.choose_appetizer()
        dinner_order_with_appetizer.choose_soup()
        dinner_order_with_appetizer.choose_dish()
        dinner_order_with_appetizer.displayOrder()


def error_check(usr_input):
    while usr_input != '2' and usr_input != '1':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for dinner combo or 2 for deluxe dinner combo: ')
    return usr_input


main()
