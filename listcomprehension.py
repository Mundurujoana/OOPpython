
#List Comprehension
#For instance if you want to change a string to a list of characters.
from time import process_time_ns


language = 'python'
lst = list(language)
print(lst)

#For instance if you want to generate a list of numbers
number = [i for i in range(11)]
print(number)

square = [i*i for i in range(20)]
print(square)

numSquare= [(i, i * i) for i in range(11)]
print(numSquare)

#List comprehension can be combined with if expression
even_numbers=[x for x in range(11) if x%2==0]
print(even_numbers)

odd_numbers = [n for n in range(11) if n%2!=0]
print(odd_numbers)

postive_numbers = [m for m in range(21) if m%2==0 and m>0]
print(postive_numbers)

# Flattening a three dimensional array
# Named function
def add_two_nums(a, b):
    return a + b

# Lets change the above function to a lambda function
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    

square = lambda x:x**2

print(square(2))

add = lambda a,b:a+b
print(add(2,8))

cube = lambda b:b**3

print(cube(4))

multiple_variable = lambda a, b, c: a*b*c
print(multiple_variable(5, 5, 3)) 

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numNeg = [d for d in numbers if d<=0 ]
print(numNeg)

# Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = list()

for sub_list in list_of_lists:
    flat_list += sub_list
print(flat_list)
