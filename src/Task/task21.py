#Palidrome of String
"""
str= input("Enter a string: ")

if str==str[::-1]:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")

"""

str=input("Enter a string: ")

rev_str=""

for char in str:
    rev_str=char+rev_str

if str==rev_str:
 print(str,"is a palindrome")
else:
 print(str,"is not a palindrome")