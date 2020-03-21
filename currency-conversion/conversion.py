import currency
# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-12-20
#
# This program is the main module for a currency conversion program.
#
# Defines a main function in the main module to do the following:
#     (1) Asks the user to choose a foreign currency: Euro, Japanese
#         Yen or Mexican Peso. Creates a loop to validate user input.
#         If an invalid choice is made, displays an error message and
#         asks the user to choose a foreign currency again until the
#         choice is valid.
#     (2) Asks the user to enter US dollar amount. Writes a loop to
#         validate user input. If the US dollar amount is negative,
#         displays an error message and asks the user to reenter it
#         until it is non-negative.
#     (3) Calls one of the three functions in the currency module to
#         convert US dollar to the foreign currency chosen by the user
#     (4) Receives and displays the converted foreign currency
#
#   The following is an example.
#
# Converting US Dollar to a foreign currency.
# Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 4
# Error: Invalid Choice
# Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 5
# Error: Invalid Choice
# Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 2
# Enter US Dollar: -100
# Error: US Dollar cannot be negative.
# Enter US Dollar: -200
# Error: US Dollar cannot be negative.
# Enter US Dollar: 100
# It is converted to 10645.0 Yen
# -----------------------------------------------------------------


def main():
    try:
        print("Converting US Dollar to a foreign currency. ")
        foreignCurrency = int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
        while foreignCurrency != 1 and foreignCurrency != 2 and foreignCurrency != 3:
            print("Error: Invalid Choice ")
            foreignCurrency = int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))

        dollarAmount = int(input("Enter US Dollar: "))
        while dollarAmount < 0:
            print("Error: US Dollar cannot be negative. ")
            dollarAmount = int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))

        if foreignCurrency == 1:
            conversion = currency.to_euro(dollarAmount)
            print("It is converted to", conversion, "Euros")
        elif foreignCurrency == 2:
            conversion = currency.to_yen(dollarAmount)
            print("It is converted to", conversion, "Yen")
        elif foreignCurrency == 3:
            conversion = currency.to_peso(dollarAmount)
            print("It is converted to", conversion, "Pesos")
    except ValueError:
        print("Error: Invalid Choice. Please restart program.")


main()
