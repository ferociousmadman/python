# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-11-20
#
# This program creates the class course. This class has the
# following three methods:
#
#    (a) An __init__ method that accepts course code and maximum
#    class size as arguments. Write statements in __init__ to
#    store them in instance variables. Also create an instance
#    variable to store enrollment and initialize it to 0.
#
#    (b) An add_student method to increase enrollment by one and
#    display “One student added” if the course is not full. If the
#    course is already full, make no change to enrollment and
#    display “Course already full”. This method has no argument
#    other than self and has no return value.
#
#    (c) A drop_student method to decrease enrollment by one and
#    display “One student dropped” if the course is not empty. If
#    the course is empty, make no change to enrollment and display
#    “Course is empty”. This method has no argument other than
#    self and has no return value.
# -----------------------------------------------------------------


class Course:

    def __init__(self, course_code, max_size):
        self.course_code = str(course_code)
        self.max_size = int(max_size)
        self.enrollment = 0

    def add_student(self):
        if self.enrollment < self.max_size:
            self.enrollment += 1
            print('One student added.')
        elif self.enrollment >= self.max_size:
            print('Course already full.')

    def drop_student(self):
        if self.enrollment > 0:
            self.enrollment -= 1
            print('One student dropped')
        elif self.enrollment == 0:
            print('Course is empty')
