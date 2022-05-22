#Write a program to check whether a person is eligible for voting or not. 
# (accept age from user)
# age = int(input("Enter age: "))

# if age >=18:
#     print("Eligible fo for voting")
# else:
#     print("Not Eligible fo for voting")

# #Write a program to check whether a number entered by user is even or odd.
# number = int(input("Enter number: "))
# if number%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# #Write a program to check whether a number is divisible by 7 or not.
# num = int(input("Enter num: "))
# if num%7==0:
#      print("Number is divisible by 7")
# else:
#     print("Number is not divisible by 7")

#Write a program to display "Hello" if a number entered by user is a multiple of five 
# ,otherwise print "Bye".
# num = int(input("Enter num: "))
# if num%5==0:
#      print("Hello")
# else:
#     print("Bye")

#Write a program to calculate the electricity bill (accept number of unit from user)
#  according to the following criteria :
            # Unit                                                     Price  
#First 100 units                                               no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)
# unit = int(input("Enter unit: "))
# amount = 0
# if unit<=100:
#    amount =0
# if unit>100 and unit<200:
#     price = 5
#     total_bill_amount = 100*5
# else:
#     print("Bye")

#. Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)
# num=int(input("Enter any number: "))
# print("Last digit of number is ",num%10)
   
#Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.
# if num%3==0:
#   print("Number is divisible by 3")
# else:
#     print("Number is not divisible by 3")

#Write a program to accept percentage from the user and display 
# the grade according to the following criteria:

        # Marks                                    Grade
        # > 90                                         A
        # > 80 and <= 90                       B
         #>= 60 and <= 80                       C
         #below 60                              D

# marks=int(input("Enter your mask: "))
# if marks>90:
#   print("A")
# elif marks > 80 and marks<= 90:
#      print("B")
# elif marks>= 60 and marks<= 80:
#      print("C")
# elif marks>60:
#   print("D")
# else:
    # print("F")

#Write a program to check whether an years is leap year or not.
# year =int(input("Enter your year: "))

# if year%400==0:
#     print("It is a leap year.")
# else:
#      print("It is not a leap year.")


#Write the output of the following if a = 9
        
    #if (a > 5 and a <=10):    
        #  print("Hello")    
    #else:    
        # print("Bye")
# a = int(input("Enter the value of a: "))
# if (a > 5 and a <=10):    
#     print("Hello")    
# else:    
#     print("Bye")

#     #Accept any city from the user and display monument of that city.
#                   #City                                 Monument
#                   #Delhi                               Red Fort
#                   #Agra                                Taj Mahal
#                   #Jaipur                              Jal Mahal

# city = input("Enter city: ")         
# if city.lower() == 'delhi':
#     print("Red Fort")   
# elif city.lower() == 'agra':
#     print("Taj Mahal") 
# elif city.lower() == 'jaipur':
#     print("Jal Mahal") 
# else:
#     print("Enter correct name of city")

#Write the logical expression for the following:
# A is greater than B and C is greater than D
print("A>B and C>D")

#Write a program to accept a number from 1 to 12 and 
# display name of the month and days in that 
# month like 1 for January and number of days 31 and so on

# num=int(input("Enter number between 1 to 12: "))
# if num==1:
#     print("January")
# elif num==2:
#     print("February")
# elif num==3:
#     print("March")
# elif num==4:
#     print("April")
# elif num==5:
#     print("May")
# elif num==6:
#     print("June")
# elif num==7:
#     print("July")
# elif num==8:
#     print("August")
# elif num==9:
#     print("September")
# elif num==10:
#     print("October")
# elif num==11:
#     print("November")
# elif num==12:
#     print("December")
# else:
#     print("Please enter number between 1 to 12")


    #Write a program to accept the cost price of a bike and 
    # display the road tax to be paid according to the following criteria :
    
        ##Cost price (in Rs)                                       Tax
        #> 100000                                                  15 %
        #> 50000 and <= 100000                          10%
        #<= 50000                                                  5%

# cost_price = int(input("Enter cost price of a bike: "))
 
# tax = 0
# if cost_price > 100000:
#    tax = 15/100*cost_price
# elif cost_price> 50000 and cost_price<= 100000:
#     tax = 10/100*cost_price 
# else:
#     tax = 5/100*cost_price
#     print(tax)

#Write a program to check a character is vowel or not
# ch=input("Enter any character: ")
# vow="aeiouAEIOU"
# if ch in vow:
#      print("Entered character is vowel")
# else:
#      print("Entered character is not vowel")

# #Write a program to check whether a number  is prime or not.
# numb=input("Enter any number: ")

# if ch in vow:
#      print("Entered character is vowel")
# else:
#      print("Entered character is not vowel")

#Accept the age of 4 people and display the oldest one.

age1=int(input("Enter age of first person"))
age2=int(input("Enter age of second person"))
age3=int(input("Enter age of third person"))
age4=int(input("Enter age of fourth person"))
if age1 > age2 and age1 > age3 and age1 > age4:
        print(age1)
if age2 > age1 and age2 > age3 and age2 > age4:
       print(age2)
if age3 > age2 and age3 > age1 and age3 > age4:
       print(age3)
if age4 > age1 and age4 > age2 and age4 > age3:
      print(age4)


#Accept the temperature in degree Celsius of water and
#check whether it is boiling or not (boiling point of water in 100 oC
# temp_celsius = int(input("Enter the degree Celsius of water: "))

# if temp_celsius>=100:
#     print("the water is boiling")
# else:
#       print("the water is not boiling")


