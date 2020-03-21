# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 1-20-20
#
# Creates program for calculating the volume of a room and the btu
# required to heat the room. Asks the user to input the room length,
# width, and height. Calculates the volume of the room, the btu needed.
# Displays the total BTU needed to heat that room and then asks if
# another calculation should be done.
# ----------------------------------------------------------------

import sys


def main():
    continue_or_end = 'Y'
    while continue_or_end != 'N':
        try:
            room_length = float(input('Enter room length: '))
            room_width = float(input('Enter room width: '))
            room_height = float(input('Enter room height: '))
            room_volume = room_length * room_width * room_height
            btu_needed = room_volume * 3.5
            print('BTU needed for this room:', format(btu_needed, ".2f"))
            continue_or_end = input('Calculate btu for another room? Enter Y for yes or N for no: ')
            print('')
            continue_or_end = continue_or_end.upper()
            if continue_or_end == 'N':
                sys.exit(0)
            elif continue_or_end == 'Y':
                pass
            else:
                continue_or_end = input('Please enter a valid response, calculate btu for another room? Enter Y for yes or N for no: ')
        except ValueError:
            print('Error: Please enter a valid response and try again. \n')


main()
