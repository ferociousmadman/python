# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-11-20
#
# This is the main module. It creates an instance of Course as a
# result of the import statement and course1 variable.
# It asks the user to enter the course code and maximum class size
# of a course. The data provided by the user is used to create an
# instance of Course. A loop is used to manage this course.
# In the loop, the user is asked to enter 1 for adding a student,
# 2 for dropping a student, 3 for displaying course info, or 0 for
# exit. If 1 is chosen, the add_student method of the Course object
# is called and then a print statement to display updated enrollment
# is used. If 2 is chosen, the drop_student method of the Course
# object is called and a print statement to display updated
# enrollment is used. If 3 is chosen, values stored in the Course
# object are displayed to show course code, maximum class size, and
# enrollment. Two error handling functions named
# max_size_error_check() and error_check() are also used in the
# main() function to ensure max_size is always an integer greater
# than 0 and that usr_input is always a valid entry.
# -----------------------------------------------------------------

from course import Course


def main():
    course_code = input('Enter course code: ')
    max_size = input('Enter maximum class size: ')
    max_size = max_size_error_check(max_size)
    course1 = Course(course_code, max_size)

    usr_input = input('Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: ')
    usr_input = error_check(usr_input)

    while usr_input != 0:
        usr_input = int(usr_input)
        if usr_input == 3:
            print('Course code:', course1.course_code)
            print('Maximum class size:', course1.max_size)
            print('Enrollment:', course1.enrollment)
            usr_input = input('\nEnter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: ')
            usr_input = error_check(usr_input)
        elif usr_input == 2:
            course1.drop_student()
            print('Enrollment:', course1.enrollment)
            usr_input = input('\nEnter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: ')
            usr_input = error_check(usr_input)
        elif usr_input == 1:
            course1.add_student()
            print('Enrollment:', course1.enrollment)
            usr_input = input('\nEnter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: ')
            usr_input = error_check(usr_input)
        elif usr_input == 0:
            pass


def error_check(usr_input):
    while usr_input != '3' and usr_input != '2' and usr_input != '1' and usr_input != '0':
        usr_input = input('Your input was ' + usr_input + ', Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: ')
    return usr_input


def max_size_error_check(max_size):
    while not max_size.isdigit() or not int(max_size) >= 1:
        max_size = input('Your input was ' + max_size + ', Enter maximum class size: ')
    return max_size


main()
