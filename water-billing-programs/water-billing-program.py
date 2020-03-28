# ----------------------------------------------------------------
# Author: Skipper Davies
# Date: 3-27-20
#
# Creates a program, which reads the data stored in “water.txt”,
# which was created in Problem 3. Calculates water charge for each
# customer. Residential customers pay $0.005 per gallon for the
# first 6000 gallons. If the usage is more than 6000 gallons, the
# rate will be $0.007 per gallon after the first 6000 gallons.
# Business customers pay $0.006 per gallon for the first 8000
# gallons. If the usage is more than 8000 gallons, the rate will
# be $0.008 per gallon after the first 8000 gallons. Displays
# account number and water charge of each customer on computer
# screen.
# ----------------------------------------------------------------


def main():

    water_file = open('water.txt', 'r')
    billing_data = []
    for line in water_file:
        line = line.strip()
        billing_data.append(line)
    water_file.close()

    count = 0
    for i in billing_data:

        account_num = ''
        iterator = 0
        for n in billing_data[count]:
            if billing_data[count][iterator].isdigit():
                account_num = account_num + billing_data[count][iterator]
            elif billing_data[count][iterator].isalpha():
                break
            iterator += 1

        account_type = ''
        iterator = 0
        for n in billing_data[count]:
            if billing_data[count][iterator].isalpha():
                account_type = billing_data[count][iterator]
            elif billing_data[count][iterator].isdigit() or billing_data[count][iterator].isspace():
                pass
            iterator += 1

        water_use = ''
        iterator = 0
        for n in billing_data[count]:
            if billing_data[count][iterator].isalpha():
                iterator = iterator + 2
                while iterator < len(billing_data[count]):
                    water_use = water_use + billing_data[count][iterator]
                    iterator += 1
                break
            elif billing_data[count][iterator].isdigit() or billing_data[count][iterator].isspace():
                pass
            iterator += 1
        water_use = int(water_use)

        if account_type == "R":
            if 0 < water_use <= 6000:
                water_charge = water_use * 0.005
            elif water_use > 6000:
                water_charge = (6000 * 0.005) + ((water_use - 6000) * 0.007)
        elif account_type == "B":
            if 0 < water_use <= 8000:
                water_charge = water_use * 0.006
            elif water_use > 8000:
                water_charge = (8000 * 0.006) + ((water_use - 8000) * 0.008)
        else:
            water_charge = "ERROR, invalid account type"
        print("Account number:", account_num, "Water charge:", water_charge)

        count += 1


main()

