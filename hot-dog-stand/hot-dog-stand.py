# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 1-21-20
#
# Creates program for a hot dog stand. Asks the user to input the
# the number of hot dogs, bags of chips, and sodas in an order.
# Calculates and displays the total amount due and then asks if
# another order should be done.
# ----------------------------------------------------------------

import sys


def main():
    continue_or_end = 'Y'
    while continue_or_end != 'N':
        try:
            num_hot_dogs = float(input('Input number of hot dogs: '))
            num_chips = float(input('Input number of bags of chips: '))
            num_sodas = float(input('Input number of sodas: '))
            total_price = (num_hot_dogs * 2.50) + (num_chips * 1.50) + (num_sodas * 1.25)
            print('Total amount due: ', format(total_price, ".2f",), '\n')
            continue_or_end = input('Input another order? Enter Y for yes or N for no: ')
            continue_or_end = continue_or_end.upper()
            if continue_or_end == 'N':
                sys.exit(0)
            elif continue_or_end == 'Y':
                pass
            else:
                continue_or_end = input('Please enter a valid response, calculate another course grade? Enter Y for yes or N for no: ')
        except ValueError:
            print('Error: Please enter a valid response and try again. \n')


main()
