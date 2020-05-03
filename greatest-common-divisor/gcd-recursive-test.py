# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 2-11-20
#
# A program that finds the greatest common divisor for any given two
# positive non-floating point integers (without if/else statements)
# and without importing math
# ----------------------------------------------------------------

import sys


def gcd(first_num, second_num):
    while first_num and second_num != 0:
        try:
            largest_num = max(first_num, second_num)
            smallest_num = min(first_num, second_num)
            gcd_num = (smallest_num, largest_num % smallest_num)
            gcd_list = list(gcd_num)
            print(gcd_list)
            first_num = gcd_list[0]
            second_num = gcd_list[1]
            while gcd_num != 0:
                try:
                    gcd(first_num, second_num)
                    break
                except ValueError:
                    print("Error")
            break

        except ValueError:
            print("Error")
        finally:
            while gcd_list[0] == 0 or gcd_list[1] == 0:
                final_value = gcd_list[0]
                print("The greatest common divisor for the entered numbers is: " + str(final_value))
                main()
                sys.exit(0)


def main():
    print("")
    con = input("Calculate a greatest common divisor? [Y/N]: ")
    con = con.upper()
    con = error_handler(con)
    while con != 'N':
        first_num = input("Please enter first number for greatest common divisor calculation: ")
        first_num = num_error_handler(first_num)
        second_num = input("Please enter second number for greatest common divisor calculation: ")
        second_num = num_error_handler(second_num)
        gcd(first_num, second_num)


def error_handler(con):
    while con != 'Y' and con != 'N':
        con = input('ERROR (must enter "Y" or "N") Calculate a greatest common divisor? [Y/N]: ')
        con = con.upper()
    return con


def num_error_handler(num):
    while not num.isdigit():
        num = input('ERROR (must enter an integer): ')
        try:
            num = int(num)
            break
        except ValueError:
            continue
    return int(num)


main()

