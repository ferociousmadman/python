# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
#
# This program creates a Deluxe_dinner_combo class for deluxe
# dinner combos. This class is a derived class of the dinner_combo
# class. It has one additional protected instance variable:
# appetizer. The program defines a choose_appetizer method to
# choose an appetizer, and a displayOrder method to display items
# ordered and the total amount due.
# -----------------------------------------------------------------

from Dinner_combo import Dinner_combo


class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self):

        super().__init__()
        self._appetizer = ''

    def choose_appetizer(self):

        usr_input = input('Enter 1 for spring roll [$1.25] or 2 for chicken wing [$1.50]: ')
        usr_input = error_check_appetizer(usr_input)
        usr_input = int(usr_input)

        if usr_input == 1:
            self._appetizer = 'spring roll ,'
            self._total += 1.25

        elif usr_input == 2:
            self._appetizer = 'chicken wing ,'
            self._total += 1.50

    def displayOrder(self):

        print('Items ordered: ' + self._appetizer, self._soup, self._main_dish, '\nPlease pay this amount: ' + str("{:.2f}".format(self._total)))


def error_check_appetizer(usr_input):

    while usr_input != '2' and usr_input != '1':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for spring roll [$1.25] or 2 for chicken wing [$1.50]: ')
    return usr_input

