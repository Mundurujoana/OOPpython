
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
if age >=18:
   print("You are old enough to drive")
else:
    print(" wait for the missing amount of years.")


# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to 
# print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
# myAge = int(input("Enter your age: "))


# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# elif num1<num2:
#      print(f"{num1} is smaller than {num2}")
# else:
#      print(f"{num1} is equal to {num2}")

#Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F
# grade = int(input("Enter grade: "))

# if grade >80:
#     print('A')
# elif grade >70 and grade<=79:
#     print('B')
# elif grade >60 and grade<=69:
#     print('c')
# elif grade >50 and grade<=59:
#     print('D')
# elif grade >0 and grade<=49:
#     print('F')
# else:
#     print('Null')


# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December,
#  January or February, the season is Winter. March, April or
# May, the season is Spring June, July or August, the season is Summer


# month = input("Enter month: ")

# if month == 'September' or 'October' or 'November':
#     print("season is Autumn")
# elif month == 'December' or 'January' or 'February':
#     print("season is Winter")
# elif month == 'March' or 'Apirl' or 'May':
#     print("season is Spring")
# elif month == 'June'or 'July' or 'August':
#     print("season is Summer")
# else:
#      print("season")


#The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# #If a fruit doesn't exist in the list add the fruit to the list and
# #  print the modified list. If the fruit exists 
# # print('That fruit already exist in the list')
# for fruit in fruits:
#  if fruit not in fruits:
#    fruit.append('carrots')
#    print(fruit)
#    print('That fruit already exist in the list')
# #  else:
   

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Check if the person dictionary has skills key, 
#if so print out the middle skill in the skills list.
print('skills' in person)
middleSkill =person[5]='Node'
print(middleSkill)

#Check if the persoAn dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
print('skills' in person)


 #If a person skills has only JavaScript and React, 
 # print('He is a front end developer'), if the person skills has Node, 
 # Python, MongoDB, print('He is a backend developer'), 
 # if the person skills has React, Node and MongoDB, 
 # Print('He is a fullstack developer'), else print('unknown title') - 
 # for more accurate results more conditions can be nested!

 #If the person is married and if he lives in Finland, 
 # print the information in the following format: