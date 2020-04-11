# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-11-20
#
# This program creates the class Drone. This class has the
# following five methods:
#
#     (a) __init__ : Creates two instance variables to store the
#     speed and the height of the drone in self.speed and
#     self.height respectively. Initialize them to 0.0.
#     This method has no parameters other than self and no return
#     value.
#
#     (b) accelerate : Increases the speed of the drone by 10.
#     There is no upper speed limit.
#     This method has no parameters other than self and no return
#     value.
#
#     (c) decelerate : Decreases the speed of the drone by 10.
#     The new speed cannot be negative. This method has no
#     parameters other than self and no return value.
#
#     (d) ascend : Increases the height of the drone by 10. There
#     is no upper height limit.
#     This method has no parameters other than self and no return
#     value.
#
#     (e) descend : Decreases the height of the drone by 10. The new
#     height cannot be negative. This method has no parameters
#     other than self and no return value.
# -----------------------------------------------------------------


class Drone:

    def __init__(self):
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        self.speed += 10

    def decelerate(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            pass

    def ascend(self):
        self.height += 10

    def descend(self):
        if self.height >= 10:
            self.height -= 10
        else:
            pass
