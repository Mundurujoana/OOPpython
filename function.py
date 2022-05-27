
# #keyword arguments
# # A keyword argument is followed by an equal sign and an expression that gives its default value.
# # Keyword arguments are arguments that can be called by their name

# def rectangle(width, height):
#     return width*height

# rectangle(width=23,height=10)

# def person(name,age):
#     print(f"my name is {name} and i am {age} years old")

# person(name='joana',age=32)

# # positional arguments
# # A positional argument is a name that is not followed by an equal sign (=) and default value.
# #Positional arguments are arguments that can be called by their position in the function call.

# def circle(pie,radius):
#     return pie*radius*radius

# circle(3.14,14)

# *args refer to regular arguments (e.g. myFun(1,2,3)).
# **kwargs refer to keyword arguments (e.g. myFun(name="Charlie")
def mySum(*args):
    s = 0
    for num in args:
        s += num
    return s

mySum(1,2)        # returns 3
mySum(1,2,2,3,4)  

def maxNum(*num):
    return max(num)

def sums(*numb):
    d = 0
    for num in numb:
        d += num
    return d


def multiply(*number):
    m = 1
    for num in number:
        m *= num
    return m



def greeting(fname='mundu', msq='good morning madam'):
    print("hello{},{}".format(fname,msq))

greeting('janet')
greeting('john', 'how are you doing')

def facrorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    return fact

word= input("Enter a word: ")
vowel = 0
if ('a'==)