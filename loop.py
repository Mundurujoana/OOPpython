# LOOPS
# While Loop
# It is used to execute a block of statements repeatedly until a given condition is satisfied.
count = 0
while count<5:
    count = count + 1
    print(count)
else:
    print(count)

    number= 1
while number <=10:
    print(number, "=", number**2)
    number = number + 1

numb = 10
while numb < 300:
    print(numb)
    numb = numb+1

    xon = 10
while xon>=0:
   print(xon)
   xon = xon-1

num = 105
while num>=7:
 print(num)
 num=num - 7

num = 10
sum = 0
while num >= 1:
   sum = sum + num
   num= num - 1
print(sum)

i = 1
num = int(input("Enter any number  : "))
while i <= 10:
    print(num," * ",i," = ", num * i)
    i = i+1

# For Loop
# Loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

    vowels = 'aeiouAEIOU'
    for ch in vowels:
        print(ch)


for num in range(10,300):
    print(num)


# Break and Continue
# We use break when we like to stop our loop before it is completed. 
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

nums=(1,2,3,4,5,6,7,8,9)
for n in nums:
    print(n)
    if n ==3:
        break

    numbers = (1,2,3,4,5,6,7)
    for a in numbers:
        print(a)
    if a ==3:
        continue

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1


# # The Range Function
# # The range() function is used list of numbers
for num in range(0,11):
    print(num)
srt = list(range(1,11,2))
print(srt)

srtone = set(range(0,21))
print(srt)

# # For Else
# # If we want to execute some message when the loop ends, we use else.
for x in range(0,12):
    print(x)
else:
    print("the loop ended")

  # Nested For Loop
 # We can write loops inside a loop.
person = {
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
for key in person:
     if key=='skills':
         for skill in person['skills']:
             print(skill)

 # Pass
 # In python when statement is required (after semicolon), 
for num in range(4):
    pass

# Iterate 0 to 10 using for loop, do the same using while loop.
for r in range(1,10):
    print(r)

from re import L


r=0
while r <=10:
    print(r)
    r = r+1


# Iterate 10 to 0 using for loop, do the same using while loop.
for m in range(10,1):
    print(m)

x =10
while x>0:
    x=x-1
    print(x)

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

listA = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for items in listA:
    print(items)

# Use for loop to iterate from 0 to 100 and print only even numbers
for d in range(0,100):
    if d%2==0:
        print(d)

k=0
while k<=100:
 if k%2==0:
    print(k)
    k=k+1

# # Use for loop to iterate from 0 to 100 and print only odd numbers
# for d in range(0,100):
#     if d%2!=0:
#         print(d)

# y=0
# while y<=100:
#  if y%2!=0:
#     print(y)
#     y=y+1

# Use for loop to iterat from 0 to 100 and
#  print the sum of all numbers.# The sum of all numbers is 5050.++__+_+++-
sum = 0
for s in range(0,101):
   sum = sum +s
print(sum)


# Use for loop to iterate from 0 to 100 and 
# print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum = 0
for g in range(0,101):
    if g%2==0:
     sum = sum +g
print(sum)

sum = 0
for u in range(0,101):
    if u%2!=0:
     sum = sum +u
print(sum)

sum = 0
for g in range(0,101):
    if g%2==0:
     sum = sum +g
  
for e in range(0,11):
    print(f"{e}*{e}={e*e}")






