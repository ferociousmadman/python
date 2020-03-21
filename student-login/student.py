def list_courses(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------
    print("Courses registered: ")
    count = 0
    if id in r_list[0]:
        print(c_list[0])
        count += 1
    elif id not in r_list:
        pass
    if id in r_list[1]:
        print(c_list[1])
        count += 1
    elif id not in r_list:
        pass
    if id in r_list[2]:
        print(c_list[2])
        count += 1
    elif id not in r_list:
        pass
    print("Total number: ", count, '\n')


def add_course(id, c_list, r_list, m_list):

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    count_zero = 0
    for i in r_list[0]:
        count_zero += 1
    count_one = 0
    for i in r_list[1]:
        count_one += 1
    count_two = 0
    for i in r_list[2]:
        count_two += 1
    course_added = input("Enter course you want to add: ")
    if course_added not in c_list:
        print("Course not found \n")
    elif course_added in c_list:
        if course_added == "CSC101" and id not in r_list[0]:
            if count_zero < m_list[0]:
                count_zero += 1
                r_list[0].append(id)
                print("Course added \n")
            elif count_zero >= m_list[0]:
                print("Course already full. \n")
        elif course_added == "CSC101" and id in r_list[0]:
            print("You are already enrolled in that course. \n")
        if course_added == "CSC102" and id not in r_list[1]:
            if count_one < m_list[1]:
                count_one += 1
                r_list[1].append(id)
                print("Course added \n")
            elif count_one >= m_list[1]:
                print("Course already full. \n")
        elif course_added == "CSC102" and id in r_list[1]:
            print("You are already enrolled in that course. \n")
        if course_added == "CSC103" and id not in r_list[2]:
            if count_two < m_list[2]:
                count_two += 1
                r_list[2].append(id)
                print("Course added \n")
            elif count_two >= m_list[2]:
                print("Course already full. \n")
        elif course_added == "CSC103" and id in r_list[2]:
            print("You are already enrolled in that course. \n")


def drop_course(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    course_dropped = input("Enter course you want to drop: ")
    if course_dropped not in c_list:
        print("Course not found \n")
    elif course_dropped in c_list:
        if course_dropped == "CSC101" and id in r_list[0]:
            r_list[0].remove(id)
            print("Course dropped \n")
        elif course_dropped == "CSC101" and id not in r_list[0]:
            print("You are not enrolled in that course. \n")
        if course_dropped == "CSC102" and id in r_list[1]:
            r_list[1].remove(id)
            print("Course dropped \n")
        elif course_dropped == "CSC102" and id not in r_list[1]:
            print("You are not enrolled in that course. \n")
        if course_dropped == "CSC103" and id in r_list[2]:
            r_list[2].remove(id)
            print("Course dropped \n")
        elif course_dropped == "CSC103" and id not in r_list[2]:
            print("You are not enrolled in that course. \n")

