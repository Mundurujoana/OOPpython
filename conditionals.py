
#CONDITIONALS
# If Condition
from time import time


a = 3
if a > 0:
    print("a is a positive number")


#If Else Condition:
a = -3
if a < 0:
    print("a is a negative number")
else:
    print("a is a positive number")
    

#f Elif Else Condition
a = 3
if a < 0:
    print("a is a negative number")
elif(a > 0):
    print("a is a positive number")
else:
    print("a is zero")


 # Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
         print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif(a == 0):
   print('A is zero')
else:
     print('A is a negative number')


#  If Condition and Logical Operators
y=8
if y > 0 and y % 2==0:
     print('y is a positive and an even number')
elif y > 0 and y % 2!=0:
     print('y is a positive number')
elif y == 0:
     print('y is a zero')
else:
     print('y is a positive number')


# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level > 9:
    print("Access granted")

else:
     print("access denied")
     

