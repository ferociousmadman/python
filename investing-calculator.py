# ----------------------------------------------------------------------------
# Author: Skipper Davies
# Date: 4-21-20
#
# This program allows the user to do a variety of investment and
# personal finance calculations. The formulae here are widely known,
# however, the sources used are:
# https://www.bankrate.com/investing/6-financial-formulas-to-help-you-succeed/
# https://www.thebalance.com/determine-return-on-investment-3140687
# This first push will be revised in the future, so that the functions which
# contain 'pass' are filled out. Commas are not recognized as valid delineators
# -----------------------------------------------------------------------------

import sys


def main():
    usr_input = 11
    while usr_input != 0:
        usr_input = input('Please enter a number to select from the following options:\n0 To end program\n1 Calculate your personal cash flow\n2 Calculate the amount of debt you are in vs income\n3 Calculate total return on an investment\n4 Calculate simple return on an investment\n5 Calculate compounding annual growth for an investment\n6 Calculate company earnings yield\n7 Calculate company return on capital\n8 Calculate inflation adjusted ROI\n9 Calculate gains or losses\n10 Calculate how long it will take for you to double your money on an investment\n')
        usr_input = error_check(usr_input)

        options_for_response = [end_program(), personal_cashflow(usr_input), personal_leverage_ratio(usr_input), total_return(), simple_return(), compound_annual_growth(), company_earnings_yield(), company_return_on_capital(), inflation_adjusted_roi(), calculate_gains_losses(), how_long_to_double_money()]
        for i in options_for_response:
            if options_for_response[i] == usr_input:
                return options_for_response[i]


def total_return():
    pass


def simple_return():
    pass


def compound_annual_growth():
    pass


def company_earnings_yield():
    pass


def company_return_on_capital():
    pass


def personal_cashflow(usr_input):
    monthly_personal_income = input('Enter your total personal income per month: ')
    monthly_personal_income = error_check_accounting(monthly_personal_income)
    monthly_personal_expenses = input('Enter your total personal expenses per month: ')
    monthly_personal_expenses = error_check_accounting(monthly_personal_expenses)
    cashflow = monthly_personal_income - monthly_personal_expenses
    print('Calculating cash flow helps you understand your true living expenses.\nNegative cash flow means you are spending more than you are bringing in.\nPositive cash flow means you are living within your means.\nYour cash flow is:', cashflow)
    while usr_input != 0:
        usr_input = input('\nPlease enter a number to select from the following options:\n0 To end program\n1 Calculate your personal cash flow\n2 Calculate the amount of debt you are in vs income\n3 Calculate total return on an investment\n4 Calculate simple return on an investment\n5 Calculate compounding annual growth for an investment\n6 Calculate company earnings yield\n7 Calculate company return on capital\n8 Calculate inflation adjusted ROI\n9 Calculate gains or losses\n10 Calculate how long it will take for you to double your money on an investment\n')
        usr_input = error_check(usr_input)


def personal_leverage_ratio(usr_input):

    monthly_debt_payments = input('Enter the total payment you make on all debt per month: ')
    monthly_debt_payments = error_check_accounting(monthly_debt_payments)
    monthly_personal_income = input('Enter your total personal income per month: ')
    monthly_personal_income = error_check_accounting(monthly_personal_income)
    leverage_ratio = monthly_debt_payments / monthly_personal_income
    print('A common standard is that your debt ratio should be no more than 33% (.33) of your income. Yours is:', leverage_ratio)
    while usr_input != 0:
        usr_input = input('\nPlease enter a number to select from the following options:\n0 To end program\n1 Calculate your personal cashflow\n2 Calculate the amount of debt you are in vs income\n3 Calculate total return on an investment\n4 Calculate simple return on an investment\n5 Calculate compounding annual growth for an investment\n6 Calculate company earnings yield\n7 Calculate company return on capital\n8 Calculate inflation adjusted ROI\n9 Calculate gains or losses\n10 Calculate how long it will take for you to double your money on an investment\n')
        usr_input = error_check(usr_input)


def inflation_adjusted_roi():
    pass


def calculate_gains_losses():
    pass


def how_long_to_double_money():
    pass


def error_check(usr_input):
    while True:
        try:
            usr_input = int(usr_input)
            if 10 >= usr_input >= 1:
                break
            elif usr_input == 0:
                sys.exit(0)
            else:
                print('ERROR: please enter a valid positive whole number 0 - 10')
                usr_input = input('Please enter a number to select from the following options:\n1 Calculate your personal cashflow\n2 Calculate the amount of debt you are in vs income\n3 Calculate total return on an investment\n4 Calculate simple return on an investment\n5 Calculate compounding annual growth for an investment\n6 Calculate company earnings yield\n7 Calculate company return on capital\n8 Calculate inflation adjusted ROI\n9 Calculate gains or losses\n10 Calculate how long it will take for you to double your money on an investment\n')
        except ValueError:
            print('ERROR: please enter a valid positive whole number 0 - 10')
            usr_input = input('Please enter a number to select from the following options:\n1 Calculate your personal cashflow\n2 Calculate the amount of debt you are in vs income\n3 Calculate total return on an investment\n4 Calculate simple return on an investment\n5 Calculate compounding annual growth for an investment\n6 Calculate company earnings yield\n7 Calculate company return on capital\n8 Calculate inflation adjusted ROI\n9 Calculate gains or losses\n10 Calculate how long it will take for you to double your money on an investment\n')
    return usr_input


def error_check_accounting(numeric_argument):
    while True:
        try:
            numeric_argument = float(numeric_argument)
            break
        except ValueError:
            numeric_argument = input('ERROR: please enter a valid integer or decimal number: ')
    return numeric_argument


def end_program():
    return 0


main()

