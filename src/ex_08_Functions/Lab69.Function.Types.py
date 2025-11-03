# user defined functions
# They will not return any value
# They will return some value
# They will have some parameters
# They will not have parameters/arugements

import math

#Built in function
Result=max(4,7)
print(Result)


#1 No Parameter and No Arugement
#No return type

def greet():
    print("Hello world")

greet()

#2 No Return type but having arugements

def greet(name):
    print("Hello " + name)


greet("ravi")

#3 No return type with default arugement

def default_arugement(name="ravi"):

     print("Hello" + name.upper() )

default_arugement("Teja")
default_arugement()

#Multiple parameters
def multiple_arugement(name1="A",name2="B"):
    print(name1, name2)


multiple_arugement()
multiple_arugement(name1="Ravi",name2="Teja")
multiple_arugement(name1="Ravi")
multiple_arugement(name2="Teja")
multiple_arugement(name2="Ravi",name1="Teja")

#Return type function

def add(a,b):
    return a+b

result = add(5,6)

print(result)

def add_two_numbres(a=30,b=20):
    print("i will add two numbers")
    return a+b
result = add_two_numbres(10,20)
print(result)

add_two_numbres()
result= add_two_numbres()
print(result)

add_two_numbres()
result= add_two_numbres(40)
print(result)