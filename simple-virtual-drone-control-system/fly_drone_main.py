# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-11-20
#
# This program creates the main module for the drone program. It
# creates an instance of Drone as a result of the import statement.
# The main() function creates a loop to control the speed and height
# of the drone. In the loop, the user is asked to enter 1 for
# acceleration, 2 for deceleration, 3 for ascending, 4 for
# descending, or 0 for exit. The appropriate method of the Drone
# object is called to change the speed or height of the drone.
# Every time the speed or height of the drone changes, the speed
# and height are displayed as integers (converted from floating point).
# A simple error handler is also defined in  the error_check()
# function to handle user errors from usr_input in main.
# -----------------------------------------------------------------


from drone import Drone


def main():
    drone1 = Drone()
    drone_speed = int(drone1.speed)
    drone_height = int(drone1.height)
    usr_input = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')

    usr_input = error_check(usr_input)

    while usr_input != 0:
        usr_input = int(usr_input)
        if usr_input == 1:
            drone1.accelerate()
            drone_speed = int(drone1.speed)
            print('Speed:', drone_speed, 'Height:', drone_height, '\n')
            usr_input = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')
            usr_input = error_check(usr_input)
        elif usr_input == 2:
            drone1.decelerate()
            drone_speed = int(drone1.speed)
            print('Speed:', drone_speed, 'Height:', drone_height, '\n')
            usr_input = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')
            usr_input = error_check(usr_input)
        elif usr_input == 3:
            drone1.ascend()
            drone_height = int(drone1.height)
            print('Speed:', drone_speed, 'Height:', drone_height, '\n')
            usr_input = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')
            usr_input = error_check(usr_input)
        elif usr_input == 4:
            drone1.descend()
            drone_height = int(drone1.height)
            print('Speed:', drone_speed, 'Height:', drone_height, '\n')
            usr_input = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')
            usr_input = error_check(usr_input)
        elif usr_input == 0:
            drone_speed = int(drone1.speed)
            drone_height = int(drone1.height)
            print('Speed:', drone_speed, 'Height:', drone_height, '\n')


def error_check(usr_input):
    while usr_input != '4' and usr_input != '3' and usr_input != '2' and usr_input != '1' and usr_input != '0':
        usr_input = input('Your input was ' + usr_input + ' Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: \n')
    return usr_input


main()
