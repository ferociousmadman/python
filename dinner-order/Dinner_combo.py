# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-18-20
#
# This program creates a Dinner_combo class for regular dinner
# combos. This class has three protected instance variables:
# main_dish, soup, and total. The program defines a choose_dish
# method to choose a main dish, a choose_soup method to choose a
# soup, and a displayOrder method to display items ordered and the
# total amount due.
# -----------------------------------------------------------------


class Dinner_combo:

    def __init__(self):

        self._soup = ''
        self._main_dish = ''
        self._total = 0.00

    def choose_dish(self):

        usr_input = input('Enter 1 for sweet and sour pork [$7], 2 for sesame chicken [$8] or 3 for shrimp fired rice [$9]: ')
        usr_input = error_check_dish(usr_input)
        usr_input = int(usr_input)

        if usr_input == 1:
            self._main_dish = 'sweet and sour pork'
            self._total += 7.00

        elif usr_input == 2:
            self._main_dish = 'sesame chicken'
            self._total += 8.00

        elif usr_input == 3:
            self._main_dish = 'shrimp fried rice'
            self._total += 9.00

    def choose_soup(self):

        usr_input = input('Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: ')
        usr_input = error_check_soup(usr_input)
        usr_input = int(usr_input)

        if usr_input == 1:
            self._soup = 'egg drop soup ,'
            self._total += 1.25

        elif usr_input == 2:
            self._soup = 'wanton soup ,'
            self._total += 1.50

    def displayOrder(self):

        print('Items ordered: ' + self._soup, self._main_dish + '\n' + 'Please pay this amount: ' + str("{:.2f}".format(self._total)))


def error_check_dish(usr_input):

    while usr_input != '3' and usr_input != '2' and usr_input != '1':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for sweet and sour pork [$7], 2 for sesame chicken [$8] or 3 for shrimp fired rice [$9]: ')
    return usr_input


def error_check_soup(usr_input):

    while usr_input != '2' and usr_input != '1':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: ')
    return usr_input

