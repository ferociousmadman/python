# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-27-20
#
# Creates program, which stores water usage data of 4 customers in
# a text file. The program asks the user to enter account number,
# customer type (R for residential or B for business), and number
# of gallons used for each of the 4 customers. Stores the data in
# a text file named “water.txt”. Overwrites old data in “water.txt”
# if the file already exists.
# ----------------------------------------------------------------


def main():

    # ------------------------------------------------------------
    # This function executes the main part of the program. It has
    # no parameter. It has been intentionally written to allow for
    # any number of integers to be entered for usr_account_number or
    # water_usage, since no limitation was given in the requirements.
    # The function starts with a while loop which uses count to check
    # to ensure that 4 customers enter their data. There are three
    # places where the user enters data, with variables where the
    # input is stored: user_account_number for the user account
    # number, user_account_type for the account type (residential or
    # business), and water_usage for how many gallons the user has
    # used. Each of these individual sections has a series of if/else
    # statements and loops for condition checking and error handling.
    # the num variable is used to iterate through two of the three
    # three while loops. Three lists are used to store the data and
    # help with inserting it into the text water.txt file for future
    # use which occurs in the writing_to_txt() function called at
    # the end of main(). The lists are passed as parameters to this
    # function.
    # -------------------------------------------------------------

    count = 0
    num = 0
    usr_account_number_list = []
    usr_account_type_list = []
    water_usage_list = []
    while count < 4:

        usr_account_number = input("Enter account number: ")
        num = 0
        while num < len(usr_account_number):
            if num < len(usr_account_number) and usr_account_number[num].isdigit():
                num += 1
            else:
                while usr_account_number[num].isalpha() or usr_account_number[num].isprintable() and not usr_account_number[num].isdigit():
                    usr_account_number = input("Please enter account number (only numbers): ")
                    num = 0
        usr_account_number_list.append(usr_account_number)

        usr_account_type = input("Enter R for residential, B for business: ")
        usr_account_type = usr_account_type.upper()
        if usr_account_type == "R":
            pass
        elif usr_account_type == "B":
            pass
        elif usr_account_type != "R" or usr_account_type != "B":
            while usr_account_type != "R" and usr_account_type != "B":
                usr_account_type = input("Enter R for residential, B for business: ")
                usr_account_type = usr_account_type.upper()
        usr_account_type_list.append(usr_account_type)

        water_usage = input("Enter number of gallons used: ")
        num = 0
        while num < len(water_usage):
            if num < len(water_usage) and water_usage[num].isdigit():
                num += 1
            else:
                while water_usage[num].isalpha() or water_usage[num].isprintable() and not water_usage[num].isdigit():
                    water_usage = input("Please enter number of gallons used (only numbers): ")
                    num = 0
        water_usage_list.append(water_usage)

        count += 1
    writing_to_txt(usr_account_number_list, usr_account_type_list, water_usage_list)


def writing_to_txt(usr_account_number_list, usr_account_type_list, water_usage_list):

    # ------------------------------------------------------------
    # This function contains three parameters, which are passed as
    # arguments from the main() function. These three arguments are
    # lists which contain the 4 customers' data which is written to
    # the water.txt file by the writing_to_txt() function.
    # -------------------------------------------------------------

    water_file = open('water.txt', 'w')
    for i in range(0, len(usr_account_type_list)):
        water_file.write(usr_account_number_list[i])
        water_file.write(' ')
        water_file.write(usr_account_type_list[i])
        water_file.write(' ')
        water_file.write(water_usage_list[i])
        water_file.write('\n')
    water_file.close()


main()
