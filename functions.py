# def greeting(name,age):
#     year = 2022-age
#     return f"My name is {name} and i am {age} years old."

# def my_country(country="Uganda",student="joana"):
#      return f"Hello {student} you are from {country}"

# my_country(country="Rwanda", student="Mercy")

# def greetMultiply(*names):
#     for name in names:
#         print("Hello {}.fnames")

#         greetMultiply("joana","Sarah","brendah","Namcy","glory")

# write a name that accepts any number of integer and return the sum ofall of them


# def add(*numbers):
#     sum=0
#     for number in numbers:
#       sum+=number
#       return sum


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