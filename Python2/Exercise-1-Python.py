tin = input('Enter Tax Identification Number: ')
if len(tin) > 9:
    print("Error! 9 characters allowed!")
elif len(tin) < 9:
    print("Error! 9 characters allowed!")
check = tin[-1]
tin = tin[:-1]
x = (int(tin[7])*(2**1))+(int(tin[6])*(2**2))+(int(tin[5])*(2**3))+(int(tin[4])*(2**4))+(int(tin[3])*(2**5))+(int(tin[2])*(2**6))+(int(tin[1])*(2**7))+(int(tin[0])*(2**8))
a = x%11
b = a%10
if (a==int(check)) and (b==int(check)):
    print('Tax Identification Number valid.')
else:
    print('Tax Identification Number invalid.')
