
#FUNCTIONS
from distutils.spawn import spawn
from re import T

# Function without Parameters
def generate_full_name():
    first_Name = "Munduru"
    last_Name = "Joana"
    space = " "
    full_Name = (first_Name+ space +last_Name)
    print(full_Name)

generate_full_name()


def add_number():
    number_one = 23
    number_two =45
    total_number = number_one+number_two
    print(total_number)

add_number()


# Function Returning a Value - Part 1
def multiply_number():
    number_one = 20
    number_two =50
    total_numb = number_one * number_two
    return(total_numb)
    
print(multiply_number())


# Function with Parameters
# In a function we can pass different data types(number,
#  string, boolean, list, tuple, dictionary or set) as a parameter
# Single Parameter: If our function takes a parameter 
# we should call our function with an argument
def greetings(name):
   message = f"Hello {name}, how are you"
   return message

print(greetings('joana'))

def  area_Of_circle(radius):
    pi = 3.14
    area = 2*pi*radius
    return area

print(area_Of_circle(20))

def sum_Of_numbers(n):
    sum =0
    for i in range(n+1):
     sum+=i
    return sum

print(sum_Of_numbers(100))


# Two Parameter:  A function may also have two or more parameters.
def identity(fullname, age):
    present_self = f"My name is {fullname} and iam {age} years old"
    return present_self

print(identity("mary susan", 24))

def average_Of_two_Numbers(num1,num2):
    sum_of_two = num1+num2
    average = sum_of_two/2.0
    return average

print(average_Of_two_Numbers(48,5))


#Passing Arguments with Key and Value
#If we pass the arguments with key and value, 
# the order of the arguments does not matte
def calculate(currentYear,bithyear):
    total_age = currentYear-bithyear
    return total_age

print(calculate(currentYear=2022,bithyear=1990))
# Returning a boolean
def evenNumber(n):
    if n%2==0:
        print("Even")
        return True
    return False

print(evenNumber(13))

# Returning a list:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))


# def greeting(name,age):
#     year = 2022-age
#     return f"My name is {name} and i am {age} years old."

# def my_country(country="Uganda",student="joana"):
#      return f"Hello {student} you are from {country}"

# my_country(country="Rwanda", student="Mercy")

#Python *args and **kwargs

def greetMultiply(*names):
    for name in names:
        print("Hello {}.fnames")

        greetMultiply("joana","Sarah","brendah","Namcy","glory")


def results(*args):
    result=0
    for i in args:
        result+=1
        return results

results(1,2,3,4,5)

def greetIngs(name, msg="how are you doing"):
    print(f"Hello {name}, {msg}")

greetIngs("joana")
greetIngs("joana","where are you goimg")



def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))



def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total

print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))


def intro(**data):
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


#default functions in python
def greet(name, msg="How do you do?"):
  print("Hello ", name + ', ' + msg)
 
greet("Ankit")
greet("Ankit", "How do you do?")
 

def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList
 
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))


def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John', 'Hello')
print(greeting)
# def greetMultiply(**kwargs):
#     print(kwargs.keys())
#     print(kwargs.values())

# greetMultiply(food="cassava",drink="juice",age="23",country="Uganda",isMarried=True)
#IT GIVES AN OUTPUT IN DICTIONARY DATASTRUCTURE.

# greetMultiply()

# def greetMultiply(**kwargs):
#     keys = kwargs.key()
#  if "name" in keys:
#     if "country" in keys:
#        print(f"Hello {kwargs["name"]} your are from {kwargs["country"]} ") 

#     elif "age" in keys:
#        year = 2022-kwargs["age"]
#         print(f"Hello {kwargs["name"] }you are born in {year})

#     elif not kwargs:
#               print("print anomyous")
 



# greetMultiply(name="susan", country="Uganda")

# greetMultiply(name="susan", age="25", school="AkiraChix")
   
# greetMultiply() f
    
# def sum_and_greet(*args, **kwargs):

#   sum=0
# for number in args:
#       sum+=number
     
# keys = kwargs.keys()
# if "name" in keys:
#        print(f" Hello {kwargs['name']} the answer is {sum}") 

# elif "country" in keys:
#         print (f" Hello {kwargs['name']}, from {kwargs['country']} the answer is {sum})

# elif not kwargs:
#            print(f"print anomyous the answer is {sum}")


# sum_and_greet(1,2,3, name='joana'):

