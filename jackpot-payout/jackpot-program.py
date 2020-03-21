# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 1-20-20
#
# This program asks for the jackpot amount (entered as a floating point number).  It
# then calculates the before and after tax installments and the before and after tax
# cash payout. 
# -----------------------------------------------------------------

jackpot_amount = float(input('Input jackpot amount (do not enter non-numerical characters aside from a decimal point if required): '))
before_tax_installments = (jackpot_amount / 20)
after_tax_installments = (jackpot_amount * .70) / 20
print('Before tax installments amount:', format(before_tax_installments,".2f"))
print('After tax installments amount:', format(after_tax_installments,".2f"))
before_tax_cash = (jackpot_amount * .65)
after_tax_cash = (jackpot_amount * .65) * .70
print('Before tax cash option amount:', format(before_tax_cash,".2f"))
print('After tax cash option amount:', format(after_tax_cash,".2f"))
