# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-25-20
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student
import sys


def main():

    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]

    while True:
        add_drop_list_courses = 1
        identify = input("Enter ID to log in, or 0 to quit: ")
        if identify == '0':
            print("Session ended.")
            sys.exit(0)
        else:
            is_login_successful = login(id=identify, s_list=student_list)
            if is_login_successful == True:
                while add_drop_list_courses != 0:
                    add_drop_list_courses = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                    if add_drop_list_courses == 3:
                        student.list_courses(id=identify, c_list=course_list, r_list=roster_list)
                    elif add_drop_list_courses == 1:
                        student.add_course(id=identify, c_list=course_list, r_list=roster_list, m_list=max_size_list)
                    elif add_drop_list_courses == 2:
                        student.drop_course(id=identify, c_list=course_list, r_list=roster_list)
                    elif add_drop_list_courses == 0:
                        print("Session ended. \n")
                        pass
                    else:
                        print("Please enter a correct option. \n")


def login(id, s_list):

    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input("Enter PIN: ")
    if (id, pin) in s_list:
        print("ID and PIN verified \n")
        return True
    else:
        print("ID or PIN incorrect \n")
        return False


main()
print("finished")
