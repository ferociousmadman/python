# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-21-20
#
# Creates program, which handles group orders for an aquarium and
# determines who wants admission to either the aquarium or the 3D
# show or both, and then determines the total due from the group.
# ----------------------------------------------------------------


def main():
    continue_or_end = 1
    while continue_or_end != 0:
        try:
            aquarium_only = int(input('Input number of people who want admission only to the aquarium, but no 3D show: '))
            show_only = int(input('Input number of people who want tickets to the 3D show, but no admission to the aquarium: '))
            both_show_aquarium = int(input('Input number of people who want both tickets to the 3D show, and also admission to the aquarium: '))
            order_aquarium = (aquarium_only * 14)
            order_show = (show_only * 8)
            order_both = (both_show_aquarium * 22) * .75
            total_due = (order_aquarium + order_show + order_both)
            print('Total due from group is:', format(total_due, ".2f"))
            continue_or_end = int(input('Enter another group? Enter 1 for yes or 0 for no: '))
        except ValueError:
            print("Error, please re-enter the information correctly. \n")


main()
