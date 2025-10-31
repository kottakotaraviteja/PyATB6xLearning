"""
Q - Create a function which will take a positive number from the user and perform square of the number?

i/o = 3

o/p = 9
"""

def square_of_a_number(number):
    if number > 0:
        print(number**2)

    else:
        print("Invalid Number")



square_of_a_number(int(input("Enter number: ")))

