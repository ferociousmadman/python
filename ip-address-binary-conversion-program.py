# For determining the 8 bit binary sequence for IP addresses. So for the IP address 154.31.16.13 the first numeric sequence is 154 and the next numeric sequence is 31, etc:
# So in this program, the IP address 154.31.16.13 would be: 10011010.00011111.00010000.00001101
# In addition, the first and firstNum variables combined with the if/else clauses determine what class the IP address is.

con = 'y'
num = ''
ipList = []

while con == 'y':
    num = int(input("Please enter one of the numeric sequences for an IP address: "))
    ipList.append(format(int(num), '08b'))
    print(*ipList, sep = '.')
    first = ipList[0]
    print(int(first,2))
    firstNum = int(first, 2)
    if 1 <= firstNum <= 127:
        print("This IP address is a Class A IP address")
    elif 128 <= firstNum <= 191:
        print("This IP address is a Class B IP address")
    elif 192 <= firstNum <= 223:
        print("This IP address is a Class C IP address")
    elif 224 <= firstNum <= 239:
        print("This IP address is a Class D IP address")
    elif 240 <= firstNum <= 254:
        print("This IP address is a Class E IP address")
    else:
        print("Error, IP address falls outside of a class designation")
    print('\n')
    con = input("Enter another numeric sequence for an IP address? [y/n]: ")
