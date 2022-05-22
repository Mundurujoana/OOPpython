# To create a dictionary we use curly brackets, {} or the dict() built-in function
empty_dic ={}
print(empty_dic)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

    # Dictionary Length, It checks the number of 'key: value' pairs in the dictionary.
lengthOfdic = len(person)
print(lengthOfdic)

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.
print(person['first_name'])

# Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary
person['status']='Single'
print(person)

# Modifying Items in a Dictionary
# We can modify items in a dictionary
person['last_name'] = 'joana'
print(person)

# Checking Keys in a Dictionary
# We use in operator to check if a key exist in a dictionary
print('address' in person) 

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
removepop = person.pop('address')
print(removepop)
print(person)

# popitem(): removes the last item
print(person.popitem())
print(person)

# del: removes an item with specified key name
del person['is_marred']
print(person)

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
print(person.items())

# Copy a Dictionary
# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
copiesdic = person.copy()
print(copiesdic)

# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
getkeyList = person.keys()
print(getkeyList)

# Getting Dictionary Values as a List
# The values method gives us all the values of a a dictionary as a list.
getvalueList = person.keys()
print(getvalueList)

# Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
print(person.clear())
print(person)

# Deleting a Dictionary
# If we do not use the dictionary we can delete it completely
del person

# Exercise
# Create an empty dictionary called dog
dog = {}
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'joana'
dog['age'] = 12
dog['school'] = 'AkiraChix'
dog['interest'] = 'dancing'
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and 
# address as keys for the dictionary
student = {}
print(student)

student['first_name'] = 'Mundu'
student['last_name'] = 'mary'
student['gender'] = 'female'
student['age'] = 34
student['marital status'] = 'married'
student['country'] = 'Uganda'
student['city'] = 'Kampala'
student['address'] = 'Nkororngo'
student['skills'] = 'HTML'

print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list


# Modify the skills values by adding one or two skills
student['skills'] = 'JavaScript','python'

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())
print(student)

# Change the dictionary to a list of tuples using items() method
print(student.items())
print(student)

# Delete one of the items in the dictionary
print(student.popitem())

# Delete one of the dictionaries
del student