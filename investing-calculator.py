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
    continue_or_end = '3'
    options_for_response = [end_program, personal_cashflow, personal_leverage_ratio, total_return, simple_return,
                            compound_annual_growth, company_earnings_yield, company_return_on_capital,
                            inflation_adjusted_roi, calculate_gains_losses, how_long_to_double_money]
    while continue_or_end != '0':
        continue_or_end = input('Enter 0 to exit or 1 for option selections: ')
        if continue_or_end == '1':
            usr_input = input('''\nPlease enter a number to select from the following options:
0 To end program
1 Calculate your personal cash flow
2 Calculate the amount of debt you are in vs income
3 Calculate total return on an investment
4 Calculate simple return on an investment
5 Calculate compounding annual growth for an investment
6 Calculate company earnings yield
7 Calculate company return on capital
8 Calculate inflation adjusted ROI
9 Calculate gains or losses
10 Calculate how long it will take for you to double your money on an investment\n''')
        elif continue_or_end == '0':
            sys.exit(0)
        else:
            continue
        usr_input = error_check(usr_input)

        options_for_response[usr_input]()


def total_return():
    value_of_investment_end_of_year = input(
        'Enter the value of investment at end of the year (no dollar signs or commas): ')
    value_of_investment_end_of_year = error_check_accounting(value_of_investment_end_of_year)
    value_of_investment_start_of_year = input(
        'Enter the value of investment at beginning of the year (no dollar signs or commas): ')
    value_of_investment_start_of_year = error_check_accounting(value_of_investment_start_of_year)
    dividends = input('Enter the value of total dividends for the year: ')
    dividends = error_check_accounting(dividends)
    result = ((value_of_investment_end_of_year - value_of_investment_start_of_year) + dividends) / value_of_investment_start_of_year
    print('You have received a ' + '{:.1%}'.format(result) + ' percent return on your investment.')


def simple_return():
    pass


def compound_annual_growth():
    pass


def company_earnings_yield():
    pass


def company_return_on_capital():
    pass


def personal_cashflow():
    monthly_personal_income = input('Enter your total personal income per month: ')
    monthly_personal_income = error_check_accounting(monthly_personal_income)
    monthly_personal_expenses = input('Enter your total personal expenses per month: ')
    monthly_personal_expenses = error_check_accounting(monthly_personal_expenses)
    cashflow = monthly_personal_income - monthly_personal_expenses
    print(
        '''Calculating cash flow helps you understand your true living expenses.
Negative cash flow means you are spending more than you are bringing in.
Positive cash flow means you are living within your means.
Your cash flow is:''',
        cashflow)


def personal_leverage_ratio():
    monthly_debt_payments = input('Enter the total payment you make on all debt per month: ')
    monthly_debt_payments = error_check_accounting(monthly_debt_payments)
    monthly_personal_income = input('Enter your total personal income per month: ')
    monthly_personal_income = error_check_accounting(monthly_personal_income)
    leverage_ratio = monthly_debt_payments / monthly_personal_income
    print('A common standard is that your debt ratio should be no more than 33% (.33) of your income. Yours is:',
          leverage_ratio)


def inflation_adjusted_roi():
    pass


def calculate_gains_losses():
    market_price = input('Enter the current market price for your investment: ')
    market_price = error_check_accounting(market_price)
    purchase_price = input('Enter the price you purchased your investment for: ')
    purchase_price = error_check_accounting(purchase_price)
    percentage_increase_or_decrease = (market_price - purchase_price) / purchase_price
    if percentage_increase_or_decrease > 0:
        print('You have a gain of: ', str('{:.1%}'.format(percentage_increase_or_decrease)) + '%')
    elif percentage_increase_or_decrease < 0:
        print('You have a loss of: ', str('{:.1%}'.format(percentage_increase_or_decrease)) + '%')
    elif percentage_increase_or_decrease == 0:
        print('You have neither a gain, nor a loss: ', str('{:.1%}'.format(percentage_increase_or_decrease)) + '%')


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
                usr_input = input(
                    '''Please enter a number to select from the following options:'
1 Calculate your personal cashflow
2 Calculate the amount of debt you are in vs income
3 Calculate total return on an investment
4 Calculate simple return on an investment
5 Calculate compounding annual growth for an investment
6 Calculate company earnings yield
7 Calculate company return on capital
8 Calculate inflation adjusted ROI
9 Calculate gains or losses
10 Calculate how long it will take for you to double your money on an investment\n''')
        except ValueError:
            print('ERROR: please enter a valid positive whole number 0 - 10')
            usr_input = input(
                '''Please enter a number to select from the following options:
1 Calculate your personal cashflow
2 Calculate the amount of debt you are in vs income
3 Calculate total return on an investment
4 Calculate simple return on an investment
5 Calculate compounding annual growth for an investment
6 Calculate company earnings yield
7 Calculate company return on capital
8 Calculate inflation adjusted ROI
9 Calculate gains or losses
10 Calculate how long it will take for you to double your money on an investment\n''')
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
