import math
a=input("Side A: ")
b=input("Side B: ")
c=input("Side C: ")
q=int(a)
w=int(b)
e=int(c)
o=math.sqrt((q+w+e)*(-q+w+e)*(q-w+e)*(q+w-e))
print(o)


