# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 1-21-20
#
# Creates program, which asks the user for the scores for 3 labs
# and two tests. It then calculates and displays the lab average,
# test average, and then calculates and displays the course grade.
# ----------------------------------------------------------------

import sys


def main():
    continue_or_end = 'Y'
    while continue_or_end == 'Y':
        try:
            lab_score_one = float(input('Input score for lab one: '))
            lab_score_two = float(input('Input score for lab two: '))
            lab_score_three = float(input('Input score for lab three: '))
            test_score_one = float(input('Input score for test one: '))
            test_score_two = float(input('Input score for test two: '))
            lab_average = (lab_score_one + lab_score_two + lab_score_three) / 3
            test_average = (test_score_one + test_score_two) / 2
            print('Lab average is:', format(lab_average,".2f") + ' and test average is:',  format(test_average, ".2f"))
            course_grade = (lab_average * .55) + (test_average * .45)
            print('Course grade is: %d' % course_grade, '\n')
            continue_or_end = input('Calculate another course grade? Enter Y for yes or N for no ')
            continue_or_end = continue_or_end.upper()
            if continue_or_end == 'N':
                sys.exit(0)
            elif continue_or_end == 'Y':
                pass
            else:
                continue_or_end = input('Please enter a valid response, calculate another course grade? Enter Y for yes or N for no ')
        except ValueError:
            print("Error: Please enter a valid response and try again. \n")


main()
