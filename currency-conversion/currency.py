# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-12-20
#
# Creates a module named currency, which includes the following
# three functions that do currency conversions:
#
# to_euro(dollar): This function receives US Dollar as an argument
# and converts it to Euro.  1 US Dollar = 0.81 Euro.  Return Euro.
#
# to_yen(dollar): This function receives US Dollar as an argument
# and converts it to Japanese Yen.  1 US Dollar = 106.45 Yen.
# Return Yen.
#
# to_peso(dollar): This function receives US Dollar as an argument
# and converts it to Mexican Peso.  1 US Dollar = 18.58 Peso.
# Return Peso.
#
# This is used by the main module named conversion.py
# ----------------------------------------------------------------


# This function receives US Dollar as an argument and converts it to Euro.  1 US Dollar = 0.81 Euro.  Return Euro.

def to_euro(dollar):
    euro = dollar * 0.81
    return euro


# This function receives US Dollar as an argument and converts it to Japanese Yen.  1 US Dollar = 106.45 Yen.  Return Yen.

def to_yen(dollar):
    yen = dollar * 106.45
    return yen


# This function receives US Dollar as an argument and converts it to Mexican Peso.  1 US Dollar = 18.58 Peso.  Return Peso.

def to_peso(dollar):
    peso = dollar * 18.
    return peso
