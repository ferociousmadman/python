# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-27-20
#
# Creates program, which asks the user to enter a string. Converts
# all letters to uppercase. Counts and displays the frequency of
# each letter in the string.
# ----------------------------------------------------------------


def main():
    usr_string = input("Enter a string: ")
    usr_string = usr_string.upper()
    count = 0
    usr_string_list = []
    for i in usr_string:
        if usr_string[count].isalpha() and count == 0:
            usr_string_list.append(usr_string[count])
            print(usr_string[count], usr_string.count(usr_string[count]))
        elif usr_string[count].isalpha() and count > 0:
            if usr_string[count] not in usr_string_list:
                print(usr_string[count], usr_string.count(usr_string[count]))
                usr_string_list.append(usr_string[count])
            elif usr_string[count] in usr_string_list:
                pass
        count += 1


main()
