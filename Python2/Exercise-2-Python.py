num = input("Enter binary number: ")

if len(num)!=8:
    print("The number you entered must have 8 digits")

else:
    numlist=[]
    sum=0

    for i in range(8):
        if int(num[i])>1:
            print("The number you entered is not binary")
            break

        else:
             numlist.append(num[i])
             numlist[i]=int(numlist[i])
             sum = sum + numlist[i]

    if sum%2==0:
        print("Parity check OK")

    else:
        print("Parity check not OK")
